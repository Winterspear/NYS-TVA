from pydantic import BaseModel
from typing import Optional

class LicenceStateOut(BaseModel):
    licenceStateID: int
    driversLicence: str
    state: str
    
    class Config:
        orm_mode = True