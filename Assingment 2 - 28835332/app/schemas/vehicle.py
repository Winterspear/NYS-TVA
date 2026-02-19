from pydantic import BaseModel
from typing import Optional

class VehicleOut(BaseModel):
    vehicleID: int
    VIN: str
    color: str
    make: str
    design: str
    manufactureyear: int
    addressID: int
    licenseStateID: int

    class Config:
        orm_mode = True