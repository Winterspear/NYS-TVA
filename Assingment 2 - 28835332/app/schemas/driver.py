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
    licenceStateID: int
    addressID: int

    class Config:
        orm_mode = True

class DriverCreate(BaseModel):
    firstName: str
    lastName: str
    birthDate: str
    heightFeet: int
    heightInches: int
    weight: int
    eyeColor: str
    licenceStateID: int
    addressID: int

class DriverUpdate(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    birthDate: Optional[str] = None
    heightFeet: Optional[int] = None
    heightInches: Optional[int] = None
    weight: Optional[int] = None
    eyeColor: Optional[str] = None
    licenceStateID: Optional[int] = None
    addressID: Optional[int] = None