from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserBase(BaseModel):
    forename: str
    surname: str
    email: str
    password: str
    driversLicence: str
    dateOfBirth: date
    phoneNumber: int
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    state: str
    zipCode: str
    VIN: str
    role: str
    



class UserCreate(UserBase):
    forename: str
    surname: str
    email: str
    password: str
    driversLicence: str
    dateOfBirth: date
    phoneNumber: str
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    state: str
    zipCode: str
    VIN: str
    role: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    phoneNumber: Optional[str] = None
    addressLine1: Optional[str] = None
    addressLine2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    VIN: Optional[str] = None

class UserOut(UserBase):
    userID: int

    class Config:
        from_attributes = True