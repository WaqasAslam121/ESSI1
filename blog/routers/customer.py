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

@router.post('/customer', status_code=status.HTTP_201_CREATED)
def createCustomer(request: schemas.Customer, db: Session = Depends(get_db)):
    new_record = models.CustomerModel(
        name= request.name, primaryContact = request.primaryContact, streetAddress = request.streetAddress,
        city = request.city, zipCode = request.zipCode, contactType = request.contactType, active = True)
    #new_record = models.ContactTypeModel(request)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get('/customer')
def get_all_customers(db: Session = Depends(get_db)):
    all_users = db.query(models.CustomerModel).all()
    return all_users    

@router.get('/customer/{id}', status_code=200)
def get_customer(id, response: Response, db: Session = Depends(get_db)):
    customer = db.query(models.CustomerModel).filter(models.CustomerModel.id == id).first()
    if not customer:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Not Available'}
    return customer

@router.put('/customer/{id}')
def update_customer(id, request: schemas.Customer, db: Session = Depends(get_db)):
    customer = db.query(models.CustomerModel).filter(models.CustomerModel.id == id).update(
        { 'name':request.name, 'primaryContact':request.primaryContact, 'streetAddress':request.streetAddress,
        'city':request.city, 'zipCode':request.zipCode, 'contactType':request.contactType, 'active':request.active})
   
    db.commit()
    return customer

@router.delete('/customer/{id}')
def delete_customer(id, db: Session = Depends(get_db)):
    record = db.query(models.CustomerModel).filter(
        models.CustomerModel.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")

    record.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'