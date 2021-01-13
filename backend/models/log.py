from datetime import datetime


class Log:
    def __init__(self, date: datetime, action: str, type_: str, id_: int = None):
        self.date = date
        self.action = action
        self.type_ = type_
        self.id_ = id_


def current_date() -> str:
    data_atual = datetime.now()
    data_completa = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_completa
