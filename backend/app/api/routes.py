from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import InventoryItem
from app.database.schemas import InventoryItemCreate

router = APIRouter()

@router.post("/inventory/")
async def create_inventory_item(item: InventoryItemCreate, db: Session = Depends(get_db)):
    new_item = InventoryItem(name=item.name, quantity=item.quantity, price=item.price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item created successfully", "item_id": new_item.id}
@router.get("/inventory/{item_id}")
async def get_inventory_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item.id, "name": item.name, "quantity": item.quantity, "price": item.price}


@router.put("/inventory/{item_id}")
async def update_inventory_item(
        item_id: int, item_update: InventoryItemCreate, db: Session = Depends(get_db)
):
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_update.name:
        item.name = item_update.name
    if item_update.quantity is not None:
        item.quantity = item_update.quantity
    if item_update.price is not None:
        item.price = item_update.price

    db.commit()
    db.refresh(item)

    return {"message": "Item updated successfully", "updated_item": {
        "id": item.id, "name": item.name, "quantity": item.quantity, "price": item.price
    }}
