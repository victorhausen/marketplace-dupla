from sqlalchemy import Column, String
from backend.models.base_model import BaseModel


class Marketplace(BaseModel):
    __tablename__ = 'marketplace'

    name = Column(String(length=200))
    description = Column(String(length=500))
   
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

# def __str__(self):
#     return f'Seller Name: {self.name} - Seller id: {self.id}