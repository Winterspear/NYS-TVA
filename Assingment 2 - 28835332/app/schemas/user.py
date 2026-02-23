from pydantic import BaseModel
from typing import Optional

class UserOut(BaseModel):
    userID: int
    username: str
    email: str
    password_hash: str
    role: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str
    role: Optional[str] = "citizen"

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    role: Optional[str] = None