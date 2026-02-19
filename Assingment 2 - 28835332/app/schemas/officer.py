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