from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .routers import masterData, users, customer

app = FastAPI()
app.include_router(masterData.router)
app.include_router(users.router)
app.include_router(customer.router)
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.BlogModel(title=request.title, body=request.body)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.BlogModel).all()
    return blogs


@app.get('/blog/{id}', status_code=200)
def get_one(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Not Available'}
    return blog


@app.delete('/blog/{id}')
def delete_blog(id, db: Session = Depends(get_db)):
    # db.query(models.BlogModel).filter(
    #    models.BlogModel.id == id).delete(synchronize_session=False)
    blog = db.query(models.BlogModel).filter(
        models.BlogModel.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'


@app.put('/blog/{id}')
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).update(
        {'title': request.title, 'body': request.body})

    #if not blog.first():
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                        detail=f"Blog with id {id} not found")
    #  blog = db.query(models.BlogModel).filter(
    #      models.BlogModel.id == id).update(request)

    # blog.update({'title': request.title, 'body': request.body})
    db.commit()

    return blog
'''