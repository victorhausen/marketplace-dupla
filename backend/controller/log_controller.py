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
        self.__dao.create(Log(datetime.now(), caller_name, action))

    def read(self) -> list:
        logs = self.__dao.read_all()
        return logs
