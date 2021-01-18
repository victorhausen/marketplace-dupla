from datetime import datetime


class Log:
    def __init__(self, date: datetime, action: str, type_: str, id_: int = None):
        self.__date = date
        self.__action = action
        self.__type_ = type_
        self.__id_ = id_

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        self.__action = action

    @property
    def type_(self):
        return self.__type_

    @type_.setter
    def type_(self, type_):
        self.__type_ = type_

    @property
    def id_(self):
        return self.__id_

    @id_.setter
    def id_(self, id_):
        self.__id_ = id_
