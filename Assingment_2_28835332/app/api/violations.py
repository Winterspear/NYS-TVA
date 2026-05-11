from app.core.security import admin_required
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.violation import violationOut
from app.crud.violation import get_violations_by_driver_id, get_all_violations, get_violations_by_violation_id
from app.core.errors import violationNotFound
from app.models.violation import Violation
from app.core.deps import get_current_user
from app.core.security import admin_required

router = APIRouter(prefix="/violations", tags=["violations"])

@router.get("/allViolations", response_model=List[violationOut])
def list_violations(db: Session = Depends(get_db)):
    return get_all_violations(db)


@router.get("/driver/{driverID}", response_model=violationOut)
def read_violation(driver_id: int, db: Session = Depends(get_db)):
    violation = get_violations_by_driver_id(db, driver_id)
    if not violation:
        raise violationNotFound(driver_id=driver_id)
    return violation

@router.get("/violation/{violationID}", response_model=violationOut)
def read_violation(violation_id: int, db: Session = Depends(get_db)):
    violation = get_violations_by_violation_id(db, violation_id)
    if not violation:
        raise violationNotFound(violation_id=violation_id)
    return violation

@router.get("/NumberOfViolations", response_model=int)
def count_violations(db: Session = Depends(get_db)):
    return len(get_all_violations(db))

@router.post("/violations/{violationID}/Create", status_code=201, response_model=violationOut)
async def create_violation(violation_in: violationOut, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    next_id = max([v.violationID for v in get_all_violations(db)], default=0) + 1
    new_violation = violationOut(next_id, **violation_in.dict())
    Violation.append(new_violation)
    return new_violation



@router.delete("/violation/{violation_id}/delete", status_code=204)
async def delete_violation(violation_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, violation in enumerate(get_all_violations(db)):
        if violation.violationID == violation_id:
            deleted_violation = violation.pop(index)
            return deleted_violation
    raise violationNotFound(violation_id=violation_id)

@router.put("/violation/violationID")
def update_violation(
    violation_id: int,
    violation_in: violationOut,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    for index, violation in enumerate(get_all_violations(db)):
        if violation.violationID == violation_id:
            updated_violation = violationOut(violation_id, **violation_in.dict())
            violation[index] = updated_violation
            return updated_violation
    raise violationNotFound(violation_id=violation_id)