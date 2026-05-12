from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.schemas.vehicle import VehicleCreate, VehicleOut
from app.crud.vehicle import get_vehicle_by_driver_id, get_all_vehicles
from app.core.errors import vehicleNotFound
from app.models.vehicle import Vehicle

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.delete("/vehicle/{vehicle_id}/delete", status_code=204)
async def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    vehicle = db.query(Vehicle).filter(Vehicle.vehicleID == vehicle_id).first()
    if not vehicle:
        raise vehicleNotFound(f"Vehicle with ID {vehicle_id} not found.")
    db.delete(vehicle)
    db.commit()


@router.put("/vehicle/{vehicle_id}/update", status_code=201, response_model=VehicleOut)
async def update_vehicle(vehicle_id: int, vehicle_in: VehicleCreate, updated: VehicleCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, v in enumerate(get_all_vehicles(db)):
        if v.vehicleID == vehicle_id:
            updated_vehicle = Vehicle(vehicle_id, **updated.dict())
            return updated_vehicle
    raise vehicleNotFound(f"Vehicle with ID {vehicle_id} not found.")