from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    quantity = Column(Integer, default=0)
    price = Column(Float)

    # Establish relationship with the User model
    user = relationship("User", back_populates="inventory")

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, nullable=False)

        # Define relationship to inventory items (one-to-many)
        inventory = relationship("InventoryItem", back_populates="user")

    def __repr__(self):
        return f"<InventoryItem(id={self.id}, name='{self.name}', quantity={self.quantity})>"
