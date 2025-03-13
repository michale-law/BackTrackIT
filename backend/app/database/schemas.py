from pydantic import BaseModel

class InventoryItemCreate(BaseModel):
    id:int
    name: str| None = None
    quantity: int| None = None
    price: float | None = None
    class Config:
        orm_mode = True