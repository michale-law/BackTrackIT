from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):  # Define User model
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    inventory_items = relationship("InventoryItem", back_populates="owner")  # Connect to inventory

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    quantity = Column(Integer, default=0)
    price = Column(Float)

    user_id = Column(Integer, ForeignKey("users.id"))  # Links each item to a user
    owner = relationship("User", back_populates="inventory_items")  # Fix relationship reference


    def __repr__(self):
        return f"<InventoryItem(id={self.id}, name='{self.name}', quantity={self.quantity})>"
