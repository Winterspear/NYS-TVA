from pydantic import BaseModel
from typing import Optional

class OfficerOut(BaseModel):
    personnelNumber: int
    firstName: str
    lastName: str
    district: int
    detachment: int

    class Config:
        from_attributes = True

class OfficerCreate(BaseModel):
    personnelNumber: int
    firstName: str
    lastName: str
    district: int
    detachment: int

class OfficerUpdate(BaseModel):
    personnelNumber: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    district: Optional[int] = None
    detachment: Optional[int] = None