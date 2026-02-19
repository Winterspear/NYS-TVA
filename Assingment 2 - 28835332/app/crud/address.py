from sqlalchemy.orm import Session
from sqlalchemy.exc import operationalError, SQLAlchemyError
from app.models.address import address
from app.core.errors import DatabaseConncectionError, DatabaseQueryError

def get_all_addresses(db: Session):
    try:
        return db.query(address).all()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch addresses from the database.")
    
def get_address_by_id(db: Session, address_id: int):
    try:
        return db.query(address).filter(address.addressID == address_id).first()
    except operationalError:
        raise DatabaseConncectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the address from the database.")