from pydantic import BaseModel

class InventoryItemCreate(BaseModel):
    name: str| None = None
    quantity: int| None = None
    price: float | None = None
