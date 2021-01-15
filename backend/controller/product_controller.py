from backend.dao_db.product_dao_db import ProductDao
from backend.controller.base_controller import BaseController


class ProductController(BaseController):
    def __init__(self):
        self.__dao = ProductDao()
        super().__init__(self.__dao, "Product")
