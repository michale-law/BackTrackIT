from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import  declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # Should be hashed

    # Relationship to inventory (if needed in future)
    inventory = relationship("InventoryProductStatus", back_populates="owner")

class InventoryProductStatus(Base):
    __tablename__ = "inventory_product_status"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    description= Column(String,index=True)
    quantity =Column(Integer)
    price = Column(Float)
    broken = Column(Integer, nullable=True, default=0)
    new = Column(Integer, nullable=True, default=0)
    used = Column(Integer, nullable=True, default=0)

    owner_id = Column(Integer, ForeignKey("users.id"))  # Link to user
    owner = relationship("User", back_populates="inventory")