from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class officer(Base):
    __tablename__ = "Officer"

    personnelNumber = Column(Integer, primary_key=True, index = True)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False)
    district = Column(String(30), nullable=False)
    detatchment = Column(String(30), nullable=False)