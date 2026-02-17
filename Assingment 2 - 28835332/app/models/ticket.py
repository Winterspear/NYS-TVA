from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base

class Violation(Base):
    __tablename__ = "Violations"

    violationID = Column(Integer, primary_key=True, index = True)
    violationDateTime = Column(DateTime, nullable=False)
    distance = Column(Integer, nullable=False)
    direction = Column(CHAR, nullable=False)
    landMark = Column(TEXT(30), nullable=False)
    road = Column(TEXT(30), nullable=False)
    violationDetails = Column(TEXT(255), nullable=False)
    actionPoint1 = Column(Boolean, nullable=False)
    actionPoint2 = Column(Boolean, nullable=False)
    actionPoint3 = Column(Boolean, nullable=False)
    personnelNumber = Column(Integer, ForeignKey(Officer.personnelNumber), nullable=False)
    driverID = Column(Integer, ForeignKey(Driver.driverID), nullable=False)