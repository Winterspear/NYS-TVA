from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class address(Base):
    __tablename__ = "Address"

    addressID = Column(Integer, primary_key=True, index = True)
    addressLine1 = Column(String(30), nullable=False)
    addressLine2 = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    state = Column(String(30), nullable=False)
    zipCode = Column(String(30), nullable=False)