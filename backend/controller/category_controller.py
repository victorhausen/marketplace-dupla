from backend.dao_db.category_dao_db import read_categories, create_category
from backend.models.category import Category


def creating_category(ca: Category) -> None:
    create_category(ca)


def reading_categories() -> list:
    categories = read_categories()
    return categories
