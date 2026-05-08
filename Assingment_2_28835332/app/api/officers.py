from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.schemas.officer import OfficerCreate, OfficerOut
from app.crud.officer import get_all_officers
from app.core.errors import officerNotFound
from app.models.officer import officer

router = APIRouter(prefix="/violations", tags=["violations"])

@router.get("/NumberOfOfficers", response_model=int)
def count_officers(db: Session = Depends(get_db)):
    return len(get_all_officers(db))