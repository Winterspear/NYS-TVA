from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from app.models.violation import Violation
from app.core.errors import DatabaseConnectionError, DatabaseQueryError

def get_all_violations(db: Session):
    try:
        return db.query(Violation).all()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch violations from the database.")

def get_violations_by_driver_id(db: Session, driver_id: int):
    try:
        return db.query(Violation).filter(Violation.DriverID == driver_id).first()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the violation from the database.")

def get_violations_by_violation_id(db: Session, violation_id: int):
    try:
        return db.query(Violation).filter(Violation.violationID == violation_id).first()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the violation from the database.")