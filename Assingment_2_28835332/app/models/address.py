from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class address(Base):
    __tablename__ = "Address"

    addressID = Column("AddressID",Integer, primary_key=True, index = True)
    addressLine1 = Column("AddressLine1",String(30), nullable=False)
    addressLine2 = Column("AddressLine2",String(30), nullable=True)
    city = Column("City",String(30), nullable=False)
    state = Column("State",String(30), nullable=False)
    zipCode = Column("ZipCode",String(30), nullable=False)