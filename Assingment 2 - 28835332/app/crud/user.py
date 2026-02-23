from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate
from app.core.security import hash_password

def get_user_be_email(db:Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def create_user(db:Session, user_in: UserCreate):
    user = UserModel(
        username=user_in.username,
        email=user_in.email,
        password_hash=hash_password(user_in.password),
        role=user_in.role or "citizen"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user