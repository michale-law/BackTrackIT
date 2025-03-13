from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    # Relationship: a user can have many inventory items
    inventory_items = relationship("InventoryItem", back_populates="owner")


class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    quantity = Column(Integer, default=0)
    price = Column(Float)

    # Foreign key linking the inventory item to a user
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationship: each inventory item is owned by one user
    owner = relationship("User", back_populates="inventory_items")

    def __repr__(self):
        return f"<InventoryItem(id={self.id}, name='{self.name}', quantity={self.quantity})>"
