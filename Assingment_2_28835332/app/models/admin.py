from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class Admin(Base):
    __tablename__ = "Admins"
    adminID = Column(Integer, primary_key=True, index = True)
    email = Column(String(30), nullable=False)
    password_hash = Column(String(300), nullable=False)