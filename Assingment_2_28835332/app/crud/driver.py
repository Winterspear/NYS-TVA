from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from app.models.driver import Driver
from app.core.errors import DatabaseConnectionError, DatabaseQueryError
from app.schemas.driver import DriverCreate

def get_all_drivers(db: Session):
    try:
        return db.query(Driver).all()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch drivers from the database.")
    
def get_driver_by_id(db: Session, driver_id: int):
    try:
        return db.query(Driver).filter(Driver.driverID == driver_id).first()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the driver from the database.")
    
def create_driver(db: Session, driver: DriverCreate):
    try:
        db_driver = Driver(
            firstName=driver.firstName,
            lastName=driver.lastName,
            birthDate=driver.birthDate,
            heightFeet=driver.heightFeet,
            heightInches=driver.heightInches,
            weight=driver.weight,
            eyeColor=driver.eyeColor,
            licenceStateID=driver.licenceStateID,
            addressID=driver.addressID
        )
        db.add(db_driver)
        db.commit()
        db.refresh(db_driver)
        return db_driver
    except SQLAlchemyError as e:
        db.rollback()
        raise e
