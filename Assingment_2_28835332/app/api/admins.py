from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.crud.admin import get_admin_by_email, create_admin
from app.schemas.admin import AdminCreate, AdminOut
from app.core.errors import userNotFound
from app.models.admin import Admin

router = APIRouter(prefix="/admins", tags=["admins"])

@app.post("")