from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.schemas.vehicle import VehicleCreate, VehicleOut
from app.crud.vehicle import create_vehicle, get_vehicles_by_driver_id, get_all_vehicles
from app.core.errors import VehicleNotFound
from app.models.vehicle import vehicle

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.delete("/vehicle/{vehicle_id}/delete", status_code=204)
async def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, v in enumerate(get_all_vehicles(db)):
        if v.vehicleID == vehicle_id:
            deleted_vehicle = v.pop(index)
            return deleted_vehicle
    raise VehicleNotFound(f"Vehicle with ID {vehicle_id} not found.")


@router.put("/vehicle/{vehicle_id}/update", status_code=201, response_model=VehicleOut)
async def update_vehicle(vehicle_id: int, vehicle_in: VehicleCreate, updated: VehicleCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, v in enumerate(get_all_vehicles(db)):
        if v.vehicleID == vehicle_id:
            updated_vehicle = vehicle(vehicle_id, **updated.dict())
            return updated_vehicle
    raise VehicleNotFound(f"Vehicle with ID {vehicle_id} not found.")