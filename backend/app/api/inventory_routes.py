from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import InventoryItemSchema  # Import schema if needed

router = APIRouter()

@router.get("/inventory/", response_model=list[InventoryItemSchema])
def get_inventory(db: Session = Depends(get_db)):
    return db.query(models.InventoryItem).all()