from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from .. import schemas
from .. import models, hashing
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

# models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post('/user', status_code=status.HTTP_201_CREATED, response_model = schemas.showUsers, tags=["User"])
def createUser(request: schemas.Users, db: Session = Depends(get_db)):
    #hashed_pwd = pwd_context.hash(request.password)
    new_record = models.UsersModel(
        name=request.name, email=request.email, password=hashing.Hash.createHash(request.password), active=True)
    #new_record = models.ContactTypeModel(request)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record



@router.get('/user',response_model = List[schemas.showUsers], tags=["User"]) #response_model = List[schemas.showUsers]
def get_all_users(db: Session = Depends(get_db)):
    all_users = db.query(models.UsersModel).all()
    return all_users    