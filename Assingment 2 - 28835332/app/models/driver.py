from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey, Date
from app.db.base import Base
from sqlalchemy.orm import relationship

class Driver(Base):
    __tablename__ = "Driver"

    driverID = Column(Integer, primary_key=True, index = True)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False)
    birthDate = Column(Date, nullable=False)
    heightFeet = Column(Integer, nullable=False)
    heightInches = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    eyeColor = Column(String(30), nullable=False)
    licenceStateID = Column(Integer, ForeignKey("LicenceState.LicenceStateID"), nullable=False)
    addressID = Column(Integer, ForeignKey("Address.AddressID"), nullable=False)