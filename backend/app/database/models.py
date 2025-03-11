from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    quantity = Column(Integer, default=0)
    price = Column(Float)

    def __repr__(self):
        return f"<InventoryItem(id={self.id}, name='{self.name}', quantity={self.quantity})>"
