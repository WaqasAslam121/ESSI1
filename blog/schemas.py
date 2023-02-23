from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ContactType(BaseModel):
    description: str
    active: bool

class BuildingType(BaseModel):
    description: str
    active: bool

class DocumentType(BaseModel):
    description: str
    active: bool

class Customer(BaseModel):
    name: str
    primaryContact: str
    streetAddress: str
    city: str
    zipCode: str
    contactType: int
    active: bool

class Users(BaseModel):
    name: str
    email: str
    password: str
    active: bool
        
class Project(BaseModel):
    name: str
    project_number: str
    project_manager: str
    site_id: int
    owner_name: str
    customer_id: int
    customer_project_manager: str
    contract_amount: str
    start_date: date
    completion_date: date
