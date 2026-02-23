from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class LicenceState(Base):
    __tablename__ = "LicenceState"

    licenceStateID = Column(Integer, primary_key=True, index = True)
    driversLicence = Column(String(30), nullable=False)
    state = Column(String(30), nullable=False)