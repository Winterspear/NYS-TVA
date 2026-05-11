from http.client import HTTPException
import os
from fastapi import Header, Depends
from app.core.errors import InvalidAPIKeyError
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = os.getenv("SECRET_KEY", "SYSAD")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext (schemes=["argon2"], deprecated = "auto")

def hash_password(password :str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, password_hash :str) -> bool:
    return pwd_context.verify(plain_password, password_hash)

def create_token(token_data: dict) -> str:
    return jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def admin_required(user=Depends(decode_token)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")