from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.db.session import get_db
from app.schemas.auth import Token
from app.crud import user as crud_user
from app.core.security import verify_password, create_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = crud_user.get_user_by_email(db, form_data.username)

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect email or password",
            headers={"WWW-Authenticate":"Bearer"})
    token_data = {
    "sub": user.email,
    "role": user.role
    }

    token = create_token(token_data)
    return {
    "access_token": token,
    "token_type": "bearer",
    "role": user.role
}