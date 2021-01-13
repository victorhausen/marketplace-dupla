from datetime import datetime


class Log:
    def __init__(self, date: datetime, action: str, type_: str, id_: int = None):
        self.date = date
        self.action = action
        self.type_ = type_
        self.id_ = id_


def current_date() -> str:
    data_atual = datetime.now()
    data_completa = data_atual.strftime("%m/%d/%Y %H:%M:%S")
    return data_completa


def format_date_to_print(date) -> str:
    date = date.strftime("%d/%m/%Y %H:%M:%S")
    return date

