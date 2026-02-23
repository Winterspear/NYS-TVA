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

class VehicleCreate(BaseModel):
    VIN: str
    color: str
    make: str
    design: str
    manufactureyear: int
    addressID: int
    licenseStateID: int

class VehicleUpdate(BaseModel):
    VIN: Optional[str] = None
    color: Optional[str] = None
    make: Optional[str] = None
    design: Optional[str] = None
    manufactureyear: Optional[int] = None
    addressID: Optional[int] = None
    licenseStateID: Optional[int] = None