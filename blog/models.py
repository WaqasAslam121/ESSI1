from sqlalchemy import Integer, Column, String, Boolean
from .database import Base


class BlogModel(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class ContactTypeModel(Base):
    __tablename__ = 'ContactType'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    active = Column(Boolean)

class CustomerModel(Base):
    __tablename__ = 'Customer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    primaryContact = Column(String)
    streetAddress = Column(String)
    city = Column(String)
    zipCode = Column(String)
    contactType = Column(Integer)
    active = Column(Boolean)

class UsersModel(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    active = Column(Boolean)