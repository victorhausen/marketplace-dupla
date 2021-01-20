from sqlalchemy import Column, String
from backend.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(length=80))
    description = Column(String(length=100))


    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
