from datetime import datetime
from sqlalchemy import Column, String, DateTime
from backend.models.base_model import BaseModel


class Log(BaseModel):
    __tablename__ = 'log'

    date = Column(DateTime)
    description = Column(String(length=500))

    def __init__(self, date: datetime, description: str):
        self.date = date
        self.description = description

