from pydantic import BaseModel
from typing import Optional

class AddressOut(BaseModel):
    addressID: int
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    zipCode: str

    class Config:
        orm_mode = True