from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.crud.user import get_user_by_email, create_user
from app.schemas.user import UserCreate, UserOut
from app.core.errors import userNotFound
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/signup", status_code=201, response_model=UserOut)
async def create_user_endpoint(user_in: UserCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        raise userNotFound(f"User with email {user_in.email} already exists.")
    return create_user(db, user_in)