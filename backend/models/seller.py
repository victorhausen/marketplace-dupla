from sqlalchemy import Column, String
from backend.models.base_model BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'


    name = Column(String(length=80))
    email = Column(String(length=50))
    phone = Column(String(length=15))

def __init__(self, name:str, email:str, phone:str):
    self.name = name
    self.email = email
    self.phone = phone

def __str__(self):
    return f'Seller Name: {self.name} - Seller id: {self.id}