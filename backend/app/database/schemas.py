from pydantic import BaseModel
from typing import Optional

# User Schema
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str  # Plain password before hashing

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Enables ORM mode

# Inventory Schema
class InventoryProductStatusBase(BaseModel):
    name: Optional[str] = None
    broken: Optional[int] = None
    new: Optional[int] = None
    used: Optional[int] = None

class InventoryProductStatusCreate(InventoryProductStatusBase):
    pass  # Used for creation

class InventoryProductStatusResponse(InventoryProductStatusBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # Enables ORM mode