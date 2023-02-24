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

@router.post('/project', status_code=status.HTTP_201_CREATED)
def createProject(request: schemas.Project, db: Session = Depends(get_db)):
    new_record = models.ProjectModel(
        name = request.name, project_number = request.project_number, project_manager = request.project_manager, site_id = request.site_id,
        owner_name = request.owner_name, customer_id = request.customer_id, customer_project_manager = request.customer_project_manager, contract_amount = request.contract_amount, start_date = request.start_date, completion_date = request.completion_date)
    #new_record = models.ContactTypeModel(request)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get('/projects')
def get_all_projects(db: Session = Depends(get_db)):
    all_projects = db.query(models.ProjectModel).all()
    return all_projects


@router.get('/project/{id}', status_code=200)
def get_project(id, response: Response, db: Session = Depends(get_db)):
    record = db.query(models.ProjectModel).filter(models.ProjectModel.id == id).first()
    if not record:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Not Available'}
    return record

@router.put('/project/{id}')
def update_project(id, request: schemas.Project, db: Session = Depends(get_db)):
    record = db.query(models.ProjectModel).filter(models.ProjectModel.id == id).update(
        { 'name': request.name, 'project_number': request.project_number, 'project_manager': request.project_manager, 'site_id': request.site_id,
        'owner_name': request.owner_name, 'customer_id': request.customer_id, 'customer_project_manager': request.customer_project_manager, 'contract_amount': request.contract_amount, 'start_date': request.start_date, 'completion_date': request.completion_date})
    db.commit()
    return record
