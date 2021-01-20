from sqlalchemy import Column, String, Numeric
from backend.models.base_model import BaseModel

class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(length=200))
    description = Column(String(length=500))
    price = Column(Numeric())

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.id = id
