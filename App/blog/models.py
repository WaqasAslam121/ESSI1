from sqlalchemy import Integer, Column, String, Boolean, Date
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

class BuildingTypeModel(Base):
    __tablename__ = 'BuildingType'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    active = Column(Boolean)

class DocumentTypeModel(Base):
    __tablename__ = 'DocumentType'
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
    
class ProjectModel(Base):
    __tablename__='Project'
    id = Column(Integer,primary_key=True, index = True)
    name = Column(String)
    project_number = Column(String)
    project_manager = Column(String)
    site_id = Column(Integer)
    owner_name = Column(String)
    customer_id = Column(Integer)
    customer_project_manager = Column(String)
    contract_amount = Column(String)
    start_date = Column(Date) 
    completion_date = Column(Date)

class SitesModel(Base):
    __tablename__='Sites'
    id = Column(Integer,primary_key=True, index = True)
    name = Column(String)
    owner_name = Column(String)
    street_address= Column(String)
    city = Column(String)
    zipCode = Column(String)
    BuildingType = Column(Integer)
    isa_campus = Column(Boolean)