from pydantic import BaseModel

class InventoryItemCreate(BaseModel):
    name: str
    quantity: int
    price: float