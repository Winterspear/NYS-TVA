from pydantic import BaseModel
from typing import Optional
from app.db.session import Session

class AddressOut(BaseModel):
    addressID: int
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    zipCode: str

    class Config:
        orm_mode = True

class AddressCreate(BaseModel):
    addressLine1 :str
    addressLine2 :str
    city :str
    state :str
    zipCode :str


class AddressUpdate(BaseModel):
    addressLine1 :Optional[str] = None
    addressLine2 :Optional[str] = None
    city :Optional[str] = None
    state :Optional[str] = None
    zipCode :Optional[str] = None