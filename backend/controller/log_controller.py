from backend.dao_db.log_dao_db import LogDao
from backend.models.log import Log
from datetime import datetime
import inspect


class LogController:
    def __init__(self):
        self.__dao = LogDao()

    def create(self, action) -> None:
        stack = inspect.stack()
        caller = stack[1]
        caller_name = caller[3]
        self.__dao.save(Log(datetime.now(), caller_name + " " + action))

    def read(self) -> list:
        logs = self.__dao.read_all()
        for log in logs:
            log.date = format_date_to_print(log.date)
        return logs


def format_date_to_print(date) -> str:
    date = date.strftime("%d/%m/%Y %H:%M:%S")
    return date