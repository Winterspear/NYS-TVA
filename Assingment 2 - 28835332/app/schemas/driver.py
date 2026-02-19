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