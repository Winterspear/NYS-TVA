from sqlalchemy import Column, Integer, String, DateTime, CHAR, TEXT, Boolean, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship

class Violation(Base):
    __tablename__ = "Violations"

    violationID = Column("ViolationID",Integer, primary_key=True, index = True)
    violationDateTime = Column("ViolationDateTime",DateTime, nullable=False)
    distance = Column("Distance",Integer, nullable=False)
    direction = Column("Direction",CHAR, nullable=False)
    landmark = Column("Landmark",TEXT(30), nullable=False)
    road = Column("Road",TEXT(30), nullable=False)
    violationDetails = Column("ViolationDetails",TEXT(255), nullable=False)
    actionPoint1 = Column("ActionPoint1",Boolean, nullable=False)
    actionPoint2 = Column("ActionPoint2",Boolean, nullable=False)
    actionPoint3 = Column("ActionPoint3",Boolean, nullable=False)
    personnelNumber = Column("PersonnelNumber",Integer, ForeignKey("Officer.PersonnelNumber"), nullable=False)
    driverID = Column("DriverID",Integer, ForeignKey("Driver.DriverID"), nullable=False)
