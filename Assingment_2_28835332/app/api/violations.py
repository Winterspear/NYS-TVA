from app.core.security import admin_required
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.violation import violationOut, violationCreate, violationUpdate
from app.crud.violation import get_violations_by_driver_id, get_all_violations, get_violations_by_violation_id
from app.core.errors import violationNotFound
from app.models.violation import Violation
from app.core.deps import get_current_user
from app.core.security import admin_required
from app.models.user import User
from app.models.driver import Driver

router = APIRouter(prefix="/violations", tags=["violations"])

@router.get("/allViolations", response_model=List[violationOut])
def list_violations(db: Session = Depends(get_db)):
    return db.query(Violation).all()


@router.get("/driver/{driver_id}", response_model=violationOut)
def read_violation_by_driver(driver_id: int, db: Session = Depends(get_db)):
    violation = get_violations_by_driver_id(db, driver_id)
    if not violation:
        raise violationNotFound(driver_id=driver_id)
    return violation

@router.get("/violation/{violation_id}", response_model=violationOut)
def read_violation_by_id(violation_id: int, db: Session = Depends(get_db)):
    violation = get_violations_by_violation_id(db, violation_id)
    if not violation:
        raise violationNotFound(violation_id=violation_id)
    return violation

@router.get("/NumberOfViolations", response_model=int)
def count_violations(db: Session = Depends(get_db)):
    return len(get_all_violations(db))

@router.post("/violations/create", status_code=201, response_model=violationOut)
async def create_violation(violation_in: violationCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_violation = Violation(**violation_in.dict())
    db.add(new_violation)
    db.commit()
    db.refresh(new_violation)
    return new_violation



@router.delete("/violation/{violation_id}")
def delete_violation(violation_id: int, db: Session = Depends(get_db)):
    violation = db.query(Violation).filter(Violation.violationID == violation_id).first()

    if not violation:
        raise violationNotFound(violation_id=violation_id)

    db.delete(violation)
    db.commit()
    return {"message": "Deleted successfully"}

@router.put("/violation/{violation_id}/update", response_model=violationOut)
def update_violation(
    violation_id: int,
    violation_in: violationUpdate,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):

    db_violation = db.query(Violation).filter(
        Violation.violationID == violation_id
    ).first()

    if not db_violation:
        raise violationNotFound(violation_id=violation_id)

    for field, value in violation_in.dict(exclude_unset=True).items():
        setattr(db_violation, field, value)

    db.commit()
    db.refresh(db_violation)

    return db_violation

@router.get("/me/violations", response_model=list[violationOut])
def get_my_violations(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return db.query(Violation)\
        .join(Driver, Violation.DriverID == Driver.driverID)\
        .join(User, User.driversLicence == Driver.driversLicence)\
        .filter(User.userID == user.userID)\
        .all()