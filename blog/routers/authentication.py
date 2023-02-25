from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from .. import schemas
from .. import models
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ["Authentication"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/login')
def login():
    return 'Login'