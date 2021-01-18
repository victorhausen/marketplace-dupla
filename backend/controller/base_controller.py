from backend.controller.log_controller import LogController


class BaseController:
    def __init__(self, dao, model_name):
        self.__log = LogController()
        self.__dao = dao
        self.__model_name = model_name

    def create(self, model: object) -> None:
        self.__dao.create(model)
        self.__log.create(self.__model_name)

    def read_by_id(self, id: int) -> object:
        model = self.__dao.read_by_id(id)
        self.__log.create(self.__model_name)
        return model

    def read_all(self) -> list:
        list_model = self.__dao.read_all()
        self.__log.create(self.__model_name)
        return list_model

    def delete(self, id: int) -> None:
        self.__dao.delete(id)
        self.__log.create(self.__model_name)

    def update(self, model: object) -> None:
        self.__dao.update(model)
        self.__log.create(self.__model_name)
