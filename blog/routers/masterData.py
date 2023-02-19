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

#ContactType -- start
@router.post('/contacttype', status_code=status.HTTP_201_CREATED)
def createContactType(request: schemas.ContactType, db: Session = Depends(get_db)):
    new_record = models.ContactTypeModel(
        description=request.description, active=True)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get('/contacttype')
def get_allContactType(db: Session = Depends(get_db)):
    types = db.query(models.ContactTypeModel).all()
    return types

@router.delete('/contacttype/{id}')
def delete_contacttype(id, db: Session = Depends(get_db)):
    record = db.query(models.ContactTypeModel).filter(
        models.ContactTypeModel.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ContactType with id {id} not found")

    record.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

@router.get('/contacttype/{id}', status_code=200)
def get_contactType(id, response: Response, db: Session = Depends(get_db)):
    record = db.query(models.ContactTypeModel).filter(models.ContactTypeModel.id == id).first()
    if not record:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Not Available'}
    return record
#ContactType --end

#BuildingType --start
@router.post('/buildingtype', status_code=status.HTTP_201_CREATED)
def createBuildingType(request: schemas.ContactType, db: Session = Depends(get_db)):
    new_record = models.BuildingTypeModel(
        description=request.description, active=True)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get('/buildingtype')
def get_allBuildingType(db: Session = Depends(get_db)):
    types = db.query(models.BuildingTypeModel).all()
    return types

@router.delete('/buildingtype/{id}')
def delete_buildingtype(id, db: Session = Depends(get_db)):
    record = db.query(models.BuildingTypeModel).filter(
        models.BuildingTypeModel.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Building Type with id {id} not found")

    record.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

@router.get('/buildingtype/{id}', status_code=200)
def get_buildingType(id, response: Response, db: Session = Depends(get_db)):
    record = db.query(models.BuildingTypeModel).filter(models.BuildingTypeModel.id == id).first()
    if not record:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Not Available'}
    return record
#BuildingType --end

#DocumentType --start
@router.post('/documenttype', status_code=status.HTTP_201_CREATED)
def createDocumentType(request: schemas.ContactType, db: Session = Depends(get_db)):
    new_record = models.DocumentTypeModel(
        description=request.description, active=True)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get('/documenttype')
def get_allDocumentType(db: Session = Depends(get_db)):
    types = db.query(models.DocumentTypeModel).all()
    return types

@router.delete('/documenttype/{id}')
def delete_documenttype(id, db: Session = Depends(get_db)):
    record = db.query(models.DocumentTypeModel).filter(
        models.DocumentTypeModel.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Document Type with id {id} not found")

    record.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

@router.get('/documenttype/{id}', status_code=200)
def get_documentType(id, response: Response, db: Session = Depends(get_db)):
    record = db.query(models.DocumentTypeModel).filter(models.DocumentTypeModel.id == id).first()
    if not record:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Not Available'}
    return record
#DocumentType --end