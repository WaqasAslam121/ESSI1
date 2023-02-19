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