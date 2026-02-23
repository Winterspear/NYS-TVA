from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.violation import ViolationOut
from app.crud.violation import get_violations_by_driver_id, get_all_violations
from app.core.errors import ViolationNotFound
from app.models.violation import violation
from app.core.deps import get_current_user

router = APIRouter(prefix="/violations", tags=["violations"])

@router.get("/", response_model=List[ViolationOut])
def list_violations(db: Session = Depends(get_db)):
    return get_all_violations(db)


@router.get("/{driver_id}", response_model=ViolationOut)
def read_violation(driver_id: int, db: Session = Depends(get_db)):
    violation = get_violations_by_driver_id(db, driver_id)
    if not violation:
        raise ViolationNotFound(driver_id=driver_id)
    return violation

@router.post("/violations/{_id}", status_code=201, response_model=ViolationOut)
async def create_violation(violation_in: ViolationOut, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    next_id = max([v.violationID for v in get_all_violations(db)], default=0) + 1
    new_violation = ViolationOut(next_id, **violation_in.dict())
    violation.append(new_violation)
    return new_violation



@router.delete("/violation/{violation_id}", status_code=204)
async def delete_violation(violation_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, violation in enumerate(get_all_violations(db)):
        if violation.violationID == violation_id:
            deleted_violation = violation.pop(index)
            return deleted_violation
    raise ViolationNotFound(violation_id=violation_id)