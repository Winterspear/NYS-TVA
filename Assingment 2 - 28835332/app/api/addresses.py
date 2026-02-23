from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_current_user
from app.db.session import get_db
from app.schemas.address import AddressCreate, AddressOut
from app.crud.address import get_all_addresses, get_address_by_id
from app.core.errors import addressNotFound
from app.models.address import address

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.post("/address/{address_id}", status_code=201, response_model=AddressOut)
async def create_address(address_in: AddressCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    next_id = max([address.addressID for address in get_all_addresses(db)], default=0) + 1
    new_address = AddressOut(next_id, **address_in.dict())
    address.append(new_address)
    return new_address


@router.put("/address/{address_id}", status_code=201, response_model=AddressOut)
async def update_address(address_id: int, address_in: AddressCreate, updated: AddressCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, address in enumerate(get_all_addresses(db)):
        if address.addressID == address_id:
            updated_address = address(address_id, **updated.dict())
            return updated_address
    raise addressNotFound(f"Address with ID {address_id} not found.")
    


@router.delete("/address/{address_id}", status_code=204)
async def delete_address(address_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    for index, address in enumerate(get_all_addresses(db)):
        if address.addressID == address_id:
            deleted_address = address.pop(index)
            return deleted_address
    raise addressNotFound(f"Address with ID {address_id} not found.")