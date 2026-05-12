from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey, Date
from app.db.base import Base
from sqlalchemy.orm import relationship

class Driver(Base):
    __tablename__ = "Driver"

    driverID = Column("DriverID",Integer, primary_key=True, index = True)
    firstName = Column("FirstName",String(30), nullable=False)
    lastName = Column("LastName",String(30), nullable=False)
    birthDate = Column("BirthDate",Date, nullable=False)
    heightFeet = Column("HeightFeet",Integer, nullable=False)
    heightInches = Column("HeightInches",Integer, nullable=False)
    weight = Column("Weight",Integer, nullable=False)
    eyeColor = Column("EyeColor",String(30), nullable=False)
    driversLicence = Column("DriversLicence",String(30), nullable=False)
    addressID = Column("AddressID",Integer, ForeignKey("Address.AddressID"), nullable=False)