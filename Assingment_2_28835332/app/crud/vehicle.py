from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from app.models.vehicle import Vehicle
from app.core.errors import DatabaseConnectionError, DatabaseQueryError

def get_all_vehicles(db: Session):
    try:
        return db.query(Vehicle).all()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch vehicles from the database.")
    
def get_vehicle_by_id(db: Session, vehicle_id: int):
    try:
        return db.query(Vehicle).filter(Vehicle.vehicleID == vehicle_id).first()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the vehicle from the database.")

def get_vehicle_by_driver_id(db: Session, driver_id: int):
    try:
        return db.query(Vehicle).filter(Vehicle.DriverID == driver_id).first()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the vehicle from the database.")