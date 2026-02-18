from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey, Year
from app.db.base import Base

class Vehicle(Base):
    __tablename__ = "Vehicle"

    vehicleID = Column(Integer, primary_key=True, index = True)
    VIN = Column(String(30), nullable=False)
    color = Column(String(30), nullable=False)
    make = Column(String(30), nullable=False)
    design = Column(String(30), nullable=False)
    manufactureyear = Column(Year, nullable=False)
    color = Column(String(30), nullable=False)
    addressID = Column(Integer, ForeignKey(address.addressID), nullable=False)
    licenseStateID = Column(Integer, ForeignKey(LicenceState.licenceStateID), nullable=False)