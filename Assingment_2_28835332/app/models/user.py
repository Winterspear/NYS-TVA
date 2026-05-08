from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey, Date
from app.db.base import Base

class User(Base):
    __tablename__ = "Users"

    userID = Column(Integer, primary_key=True, index = True)
    forename = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password_hash = Column(String(300), nullable=False)
    driversLicence = Column(String(30), nullable=False)
    dateOfBirth= Column(Date, nullable=False)
    phoneNumber = Column(Integer, nullable=False)
    addressLine1 = Column(String(30), nullable=False)
    addressLine2 = Column(String(30), nullable=True)
    city = Column(String(30), nullable=False)
    state = Column(String(30), nullable=False)
    zipCode = Column(String(30), nullable=False)
    VIN = Column(String(30), nullable=False)
    role = Column(String(30), nullable=False)