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


@router.post('/contacttype', status_code=status.HTTP_201_CREATED)
def createContactType(request: schemas.ContactType, db: Session = Depends(get_db)):
    new_record = models.ContactTypeModel(
        description=request.description, active=True)
    #new_record = models.ContactTypeModel(request)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


@router.get('/contacttype')
def get_all(db: Session = Depends(get_db)):
    types = db.query(models.ContactTypeModel).all()
    return types
