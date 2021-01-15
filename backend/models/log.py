from datetime import datetime


class Log:
    def __init__(self, date: datetime, action: str, type_: str, id_: int = None):
        self.date = date
        self.action = action
        self.type_ = type_
        self.id_ = id_




