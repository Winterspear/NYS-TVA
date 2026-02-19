from pydantic import BaseModel
from typing import Optional

class violationOut(BaseModel):
    violationID: int
    violationDateTime: str
    distance: int
    direction: str
    landMark: str
    road: str
    violationDetails: str
    actionPoint1: bool
    actionPoint2: bool
    actionPoint3: bool
    personnelNumber: int
    driverID: int

    class Config:
        orm_mode = True