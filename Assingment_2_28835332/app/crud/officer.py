from sqlalchemy.orm import Session
from sqlalchemy.exc import operationalError, SQLAlchemyError
from app.models.officer import officer
from app.core.errors import DatabaseConncectionError, DatabaseQueryError

def get_all_officers(db: Session):
    try:
        return db.query(officer).all()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch officers from the database.")

def get_officer_by_personnel_number(db: Session, personnelNumber: int):
    try:
        return db.query(officer).filter(officer.personnelNumber == personnelNumber).first()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the officer from the database.")