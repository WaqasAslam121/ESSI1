from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from .. import schemas
from .. import models
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

# models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/sites', status_code=status.HTTP_201_CREATED, tags=["Sites"])
def createSite(request: schemas.Sites, db: Session = Depends(get_db)):
    new_record = models.SitesModel(
        name = request.name, owner_name = request.owner_name, street_address = request.street_address, city = request.city,
        zipCode = request.zipCode, BuildingType = request.BuildingType, isa_campus = request.isa_campus)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get('/sites', tags=["Sites"])
def get_all_sites(db: Session = Depends(get_db)):
    all_projects = db.query(models.SitesModel).all()
    return all_projects


@router.get('/sites/{id}', status_code=200, tags=["Sites"])
def get_site(id, response: Response, db: Session = Depends(get_db)):
    record = db.query(models.SitesModel).filter(models.SitesModel.id == id).first()
    if not record:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Not Available'}
    return record

@router.put('/sites/{id}', tags=["Sites"])
def update_project(id, request: schemas.Sites, db: Session = Depends(get_db)):
    record = db.query(models.SitesModel).filter(models.SitesModel.id == id).update(
        { 'name': request.name, 'owner_name': request.owner_name, 'street_address': request.street_address, 'city': request.city,
        'zipCode': request.zipCode, 'BuildingType': request.BuildingType, 'isa_campus': request.isa_campus})
    db.commit()
    return record
