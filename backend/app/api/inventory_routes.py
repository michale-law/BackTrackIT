from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import InventoryItemSchema  # Import schema if needed
from auth import get_current_user
router = APIRouter()

@router.get("/inventory/", response_model=list[InventoryItemSchema])
def get_inventory(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.InventoryItem).filter(models.InventoryItem.user_id == current_user.id).all()
    
@router.put("/inventory/{id}", response_model=InventoryItemSchema)
def update_inventory_item(id: int, item_data: InventoryItemSchema, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == id, models.InventoryItem.user_id == current_user.id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found or access denied")

    item.name = item_data.name
    item.description = item_data.description
    item.quantity = item_data.quantity
    item.price = item_data.price

    db.commit()
    db.refresh(item)
    return item
    
@router.delete("/inventory/{id}")
def delete_inventory_item(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == id, models.InventoryItem.user_id == current_user.id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found or access denied")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}
    
    
    
    
    