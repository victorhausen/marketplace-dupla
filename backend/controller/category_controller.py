# from ..dao_txt.category_dao_txt import get_categories, create_category
from backend.dao_db.category_dao_db import get_categories, create_category
from backend.controller.log_controller import write_log
from backend.models.category import Category


def creating_category(ca: Category) -> None:
    create_category(ca)
    write_log(action="create", type="category")


def list_categories() -> list:
    categories = get_categories()
    write_log(action="list", type="categories")
    return categories
