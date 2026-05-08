from sqlalchemy.orm import Session
from app.models.admin import Admin as AdminModel
from app.schemas.admin import AdminCreate
from app.core.security import hash_password

def get_admin_by_email(db:Session, email: str):
    return db.query(AdminModel).filter(AdminModel.email == email).first()

def create_admin(db:Session, admin_in: AdminCreate):
    admin = AdminModel(
        email=admin_in.email,
        password_hash=hash_password(admin_in.password)
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin