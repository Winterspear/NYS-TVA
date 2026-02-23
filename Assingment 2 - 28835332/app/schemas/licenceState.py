from pydantic import BaseModel
from typing import Optional

class LicenceStateOut(BaseModel):
    licenceStateID: int
    driversLicence: str
    state: str
    
    class Config:
        orm_mode = True

class LicenceStateCreate(BaseModel):
    driversLicence: str
    state: str

class LicenceStateUpdate(BaseModel):
    driversLicence: Optional[str] = None
    state: Optional[str] = None