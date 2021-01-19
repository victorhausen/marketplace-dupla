from backend.models.seller import Seller
from backend.dao_db.base_dao import BaseDao


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
