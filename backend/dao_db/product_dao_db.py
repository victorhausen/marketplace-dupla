from backend.models.product import Product
from backend.dao_db.base_dao import BaseDao

class ProductDao(BaseDao):
   def __init__(self):
       super().__init__(Product)