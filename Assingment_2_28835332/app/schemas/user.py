from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    userID: int
    



class UserCreate(UserBase):
    forename: str
    surname: str
    email: str
    password: str
    driversLicence: str
    dateOfBirth: str
    phoneNumber: int
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    state: str
    zipCode: str
    VIN: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password_hash: Optional[str] = None
    phoneNumber: Optional[int] = None
    addressLine1: Optional[str] = None
    addressLine2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    VIN: Optional[str] = None

class UserOut(UserBase):
    userID: int
    forename: str
    surname: str
    email: str

    class Config:
        orm_mode = True