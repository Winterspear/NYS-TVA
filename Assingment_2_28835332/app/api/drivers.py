from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.schemas.driver import DriverCreate, DriverOut
from app.crud.driver import create_driver, get_driver_by_id, get_all_drivers
from app.core.errors import DriverNotFound
from app.models.driver import driver

router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.get("/all_drivers", response_model=List[DriverOut])
def list_drivers(db: Session = Depends(get_db)):
    return get_all_drivers(db)


@router.put("/driver/{driver_id}", status_code=201, response_model=DriverOut)
async def update_driver(driver_id: int, driver_in: DriverCreate, updated: DriverCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, d in enumerate(get_all_drivers(db)):
        if d.driverID == driver_id:
            updated_driver = driver(driver_id, **updated.dict())
            return updated_driver
    raise DriverNotFound(f"Driver with ID {driver_id} not found.")