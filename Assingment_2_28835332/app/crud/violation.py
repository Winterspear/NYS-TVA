from sqlalchemy.orm import Session
from sqlalchemy.exc import operationalError, SQLAlchemyError
from app.models.violation import Violation
from app.core.errors import DatabaseConncectionError, DatabaseQueryError

def get_all_violations(db: Session):
    try:
        return db.query(Violation).all()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch violations from the database.")

def get_violation_by_id(db: Session, violation_id: int):
    try:
        return db.query(Violation).filter(Violation.violationID == violation_id).first()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the violation from the database.")