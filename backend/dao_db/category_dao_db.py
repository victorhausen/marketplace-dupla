from backend.models.category import Category
from backend.dao_db.base_dao import BaseDao


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
