from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.violation import ViolationOut
from app.crud.violation import get_violations_by_driver_id, get_all_violations
from app.core.errors import ViolationNotFound
