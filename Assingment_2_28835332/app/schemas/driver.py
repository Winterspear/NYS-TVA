from pydantic import BaseModel
from typing import Optional

class DriverOut(BaseModel):
    driverID: int
    firstName: str
    lastName: str
    birthDate: str
    heightFeet: int
    heightInches: int
    weight: int
    eyeColor: str
    driversLicence: str
    addressID: int

    class Config:
        from_attributes = True

class DriverCreate(BaseModel):
    firstName: str
    lastName: str
    birthDate: str
    heightFeet: int
    heightInches: int
    weight: int
    eyeColor: str
    driversLicence: str
    addressID: int

class DriverUpdate(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    birthDate: Optional[str] = None
    heightFeet: Optional[int] = None
    heightInches: Optional[int] = None
    weight: Optional[int] = None
    eyeColor: Optional[str] = None
    driversLicence: Optional[str] = None
    addressID: Optional[int] = None