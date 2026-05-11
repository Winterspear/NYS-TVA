from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from app.models.address import address
from app.core.errors import DatabaseConnectionError, DatabaseQueryError

def get_all_addresses(db: Session):
    try:
        return db.query(address).all()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch addresses from the database.")
    
def get_address_by_id(db: Session, address_id: int):
    try:
        return db.query(address).filter(address.addressID == address_id).first()
    except OperationalError:
        raise DatabaseConnectionError("Cannot connect to the database.")
    except SQLAlchemyError:
        raise DatabaseQueryError("Failed to fetch the address from the database.")