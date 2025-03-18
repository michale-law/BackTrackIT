# app/database/schemas.py

from pydantic import BaseModel
from typing import Optional

# ------------------------------------------------
# USER SCHEMAS
# ------------------------------------------------
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str  # Plain password before hashing

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Enables ORM mode (attribute access)

# ------------------------------------------------
# INVENTORY PRODUCT STATUS SCHEMAS
# ------------------------------------------------
class InventoryProductStatusBase(BaseModel):
    name: Optional[str] = None
    broken: Optional[int] = None
    new: Optional[int] = None
    used: Optional[int] = None

class InventoryProductStatusCreate(InventoryProductStatusBase):
    pass

class InventoryProductStatusResponse(InventoryProductStatusBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# ------------------------------------------------
# INVENTORY ITEM SCHEMAS
# ------------------------------------------------
class InventoryItemBase(BaseModel):
    """Fields shared by create and update."""
    name: str
    description: Optional[str] = None
    quantity: int
    price: float

class InventoryItemCreate(InventoryItemBase):
    """Fields required to create a new InventoryItem."""
    pass

class InventoryItemSchema(InventoryItemBase):
    """Fields returned to the client when reading an InventoryItem."""
    id: int
    user_id: int  # or 'owner_id' if your model column is named that way

    class Config:
        from_attributes = True  # so Pydantic can read ORM model attributes
