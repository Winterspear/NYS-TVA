from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey, Date
from app.db.base import Base

class User(Base):
    __tablename__ = "Users"

    userID = Column("UserID",Integer, primary_key=True, index = True)
    forename = Column("Forename",String(30), nullable=False)
    surname = Column("Surname",String(30), nullable=False)
    email = Column("Email",String(30), nullable=False)
    password = Column("Password",String(300), nullable=False)
    driversLicence = Column("DriversLicence",String(30), nullable=False)
    dateOfBirth= Column("DateOfBirth",Date, nullable=False)
    phoneNumber = Column("PhoneNumber",String(20), nullable=False)
    addressLine1 = Column("AddressLine1",String(30), nullable=False)
    addressLine2 = Column("AddressLine2",String(30), nullable=True)
    city = Column("City",String(30), nullable=False)
    state = Column("State",String(30), nullable=False)
    zipCode = Column("ZipCode",String(30), nullable=False)
    VIN = Column("VIN",String(30), nullable=False)
    role = Column("Role",String(30), nullable=False)