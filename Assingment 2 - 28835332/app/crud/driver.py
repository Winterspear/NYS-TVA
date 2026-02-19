from sqlalchemy.orm import Session
from sqlalchemy.exc import operationalError, SQLAlchemyError
from app.models.driver import driver
from app.core.errors import DatabaseConncectionError, DatabaseQueryError

def get_all_drivers(db: Session):
    try:
        return db.query(driver).all()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch drivers from the database.")
    
def get_driver_by_id(db: Session, driver_id: int):
    try:
        return db.query(driver).filter(driver.driverID == driver_id).first()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the driver from the database.")