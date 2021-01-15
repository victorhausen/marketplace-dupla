from backend.dao_db.seller_dao_db import SellerDao
from backend.controller.base_controller import BaseController


class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao, "Seller")
