from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship

class Vehicle(Base):
    __tablename__ = "Vehicle"

    vehicleID = Column("VehicleID",Integer, primary_key=True, index = True)
    VIN = Column("VIN",String(30), nullable=False)
    color = Column("Color",String(30), nullable=False)
    make = Column("Make",String(30), nullable=False)
    design = Column("Design",String(30), nullable=False)
    manufactureyear = Column("ManufactureYear",Integer, nullable=False)
    addressID = Column("AddressID",Integer, ForeignKey("address.addressID"), nullable=False)
    DriverID = Column("DriverID",Integer, ForeignKey("Driver.DriverID"), nullable=False)