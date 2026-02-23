from pydantic import BaseModel
from typing import Optional

class OfficerOut(BaseModel):
    personnelNumber: int
    firstName: str
    lastName: str
    district: str
    detatchment: str

    class Config:
        orm_mode = True

class OfficerCreate(BaseModel):
    personnelNumber: int
    firstName: str
    lastName: str
    district: str
    detatchment: str

class OfficerUpdate(BaseModel):
    personnelNumber: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    district: Optional[str] = None
    detatchment: Optional[str] = None