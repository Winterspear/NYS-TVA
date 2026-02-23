from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str
    role: Optional[str] = "citizen"

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    role: Optional[str] = None

class UserOut(UserBase):
    userID: int
    role: str

    class Config:
        orm_mode = True