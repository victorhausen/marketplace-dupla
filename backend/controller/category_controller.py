from backend.dao_db.category_dao_db import read_categories, create_category
from backend.models.category import Category
from backend.controller.log_controller import creating_log
from backend.models.log import Log, current_date


def creating_category(ca: Category) -> None:
    create_category(ca)
    creating_log(Log(current_date(), 'create', 'category'))


def reading_categories() -> list:
    categories = read_categories()
    creating_log(Log(current_date(), 'list', 'category'))
    return categories
