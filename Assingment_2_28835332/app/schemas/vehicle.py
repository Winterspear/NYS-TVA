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
    DriversLicence: str

    class Config:
        from_attributes = True

class VehicleCreate(BaseModel):
    VIN: str
    color: str
    make: str
    design: str
    manufactureyear: int
    addressID: int
    DriversLicence: str

class VehicleUpdate(BaseModel):
    VIN: Optional[str] = None
    color: Optional[str] = None
    make: Optional[str] = None
    design: Optional[str] = None
    manufactureyear: Optional[int] = None
    addressID: Optional[int] = None
    DriversLicence: Optional[str] = None