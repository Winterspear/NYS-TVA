from pydantic import BaseModel
from typing import Optional

class AdminBase(BaseModel):
    email: str


class AdminCreate(AdminBase):
    password: str
    email: str

class AdminUpdate(BaseModel):
    email: Optional[str] = None
    password_hash: Optional[str] = None

class AdminOut(AdminBase):
    adminID: int
    email: str

    class Config:
        orm_mode = True