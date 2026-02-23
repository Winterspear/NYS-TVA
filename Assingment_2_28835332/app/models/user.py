from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class User(Base):
    __tablename__ = "Users"

    userID = Column(Integer, primary_key=True, index = True)
    username = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password_hash = Column(String(300), nullable=False)
    role = Column(String(30), nullable=False)