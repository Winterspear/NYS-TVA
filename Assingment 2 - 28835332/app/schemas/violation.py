from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class violationOut(BaseModel):
    violationID: int
    violationDateTime: datetime
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

class violationCreate(BaseModel):
    violationDateTime: datetime
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

class violationUpdate(BaseModel):
    violationDateTime: Optional[datetime] = None
    distance: Optional[int] = None
    direction: Optional[str] = None
    landMark: Optional[str] = None
    road: Optional[str] = None
    violationDetails: Optional[str] = None
    actionPoint1: Optional[bool] = None
    actionPoint2: Optional[bool] = None
    actionPoint3: Optional[bool] = None
    personnelNumber: Optional[int] = None
    driverID: Optional[int] = None