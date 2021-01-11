from ..dao_txt.category_dao_txt import get_categories, create_category
from ..dao_db.category_dao_db import get_categories_db, create_category_db

def creating_category(category) -> None:
    create_category(category)

def list_categories() -> list:
    categories = get_categories()
    return categories

def creating_category_db(category) -> None:
    create_category_db(category)

def list_categories_db() -> list:
    categories = get_categories_db()
    return categories