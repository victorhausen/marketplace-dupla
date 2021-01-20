from backend.controller.log_controller import LogController
from backend.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao, model_name):
        #self.__log = LogController()
        self.__dao = dao
        self.__model_name = model_name

    def save(self, model: BaseModel) -> None:
        self.__dao.save(model)
        #self.__log.create(self.__model_name)

    def read_by_id(self, id: int) -> object:
        model = self.__dao.read_by_id(id)
        #self.__log.create(self.__model_name)
        return model

    def read_all(self) -> list:
        list_model = self.__dao.read_all()
        #self.__log.create(self.__model_name)
        return list_model

    def delete(self, model:BaseModel) -> None:
        self.__dao.delete(model)
        #self.__log.create(self.__model_name)

    def update(self, model: BaseModel) -> None:
        self.__dao.save(model)
        #self.__log.create(self.__model_name)
