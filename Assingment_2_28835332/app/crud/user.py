from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate
from app.core.security import hash_password

def get_user_by_email(db:Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()
def get_user_by_driversLicence(db:Session, driversLicence: str):
    return db.query(UserModel).filter(UserModel.driversLicence == driversLicence).first()
def get_user_by_id(db:Session, user_id: int):
    return db.query(UserModel).filter(UserModel.userID == user_id).first()

def create_user(db:Session, user_in: UserCreate):
    user = UserModel(
        email=user_in.email,
        password=hash_password(user_in.password),
        forename=user_in.forename,
        surname=user_in.surname,
        driversLicence=user_in.driversLicence,
        dateOfBirth=user_in.dateOfBirth,
        phoneNumber=user_in.phoneNumber,
        addressLine1=user_in.addressLine1,
        addressLine2=user_in.addressLine2,
        city=user_in.city,
        state=user_in.state,
        zipCode=user_in.zipCode,
        VIN=user_in.VIN,
        role=user_in.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user