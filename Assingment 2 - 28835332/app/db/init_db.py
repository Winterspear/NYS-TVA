from app.db.base import Base
from app.db.session import engine

from app.models.address import address
from app.models.driver import Driver
from app.models.licenceState import LicenceState
from app.models.officer import officer
from app.models.vehicle import Vehicle
from app.models.violation import violation

def init_db():
    Base.metadata.create_all(bind=engine)