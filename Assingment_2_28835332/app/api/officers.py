from app.core.security import admin_required
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.schemas.officer import OfficerCreate, OfficerOut, OfficerUpdate
from app.crud.officer import get_all_officers
from app.core.errors import officerNotFound
from app.models.officer import officer

router = APIRouter(prefix="/officers", tags=["officers"])

@router.get("/NumberOfOfficers", response_model=int)
def count_officers(db: Session = Depends(get_db)):
    return len(get_all_officers(db))

@router.get("/AllOfficers", response_model=List[OfficerOut], )
def read_officers(db: Session = Depends(get_db), user=Depends(admin_required)):
    officers = get_all_officers(db)
    if not officers:
        raise officerNotFound()
    return officers

@router.get("/find/{personnelNumber}", response_model=OfficerOut)
def read_officer(personnelNumber: int, db: Session = Depends(get_db), user=Depends(admin_required)):
    db_officer = db.query(officer).filter(officer.personnelNumber == personnelNumber).first()
    if not db_officer:
        raise officerNotFound()
    return db_officer

@router.put("/update/{personnelNumber}", response_model=OfficerOut)
def update_officer(personnelNumber: int, officer_update: OfficerUpdate, db: Session = Depends(get_db), user=Depends(admin_required)):
    db_officer = db.query(officer).filter(officer.personnelNumber == personnelNumber).first()
    if not db_officer:
        raise officerNotFound()
    if officer_update.firstName is not None:
        db_officer.firstName = officer_update.firstName

    if officer_update.lastName is not None:
        db_officer.lastName = officer_update.lastName

    if officer_update.district is not None:
        db_officer.district = officer_update.district

    if officer_update.detachment is not None:
        db_officer.detachment = officer_update.detachment
    db.commit()
    db.refresh(db_officer)
    return db_officer