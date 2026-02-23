from sqlalchemy.orm import Session
from sqlalchemy.exc import operationalError, SQLAlchemyError
from app.models.vehicle import vehicle
from app.core.errors import DatabaseConncectionError, DatabaseQueryError

def get_all_vehicles(db: Session):
    try:
        return db.query(vehicle).all()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch vehicles from the database.")
    
def get_vehicle_by_id(db: Session, vehicle_id: int):
    try:
        return db.query(vehicle).filter(vehicle.vehicleID == vehicle_id).first()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the vehicle from the database.")