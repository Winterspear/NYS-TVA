from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class officer(Base):
    __tablename__ = "Officer"

    personnelNumber = Column("PersonnelNumber",Integer, primary_key=True, index = True)
    firstName = Column("FirstName",String(30), nullable=False)
    lastName = Column("LastName",String(30), nullable=False)
    district = Column("District",Integer, nullable=False)
    detachment = Column("Detachment",Integer, nullable=False)