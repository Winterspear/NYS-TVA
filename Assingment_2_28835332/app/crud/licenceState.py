from sqlalchemy.orm import Session
from sqlalchemy.exc import operationalError, SQLAlchemyError
from app.models.licenceState import LicenceState
from app.core.errors import DatabaseConncectionError, DatabaseQueryError

def get_all_licence_states(db: Session):
    try:
        return db.query(LicenceState).all()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch licence states from the database.")
    
def get_licence_state_by_id(db: Session, licence_state_id: int):
    try:
        return db.query(LicenceState).filter(LicenceState.licenceStateID == licence_state_id).first()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the licence state from the database.")
    