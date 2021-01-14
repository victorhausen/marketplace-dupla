from backend.dao_db.category_dao_db import read_categories, create_category, update_categories, delete_categories, read_categories_by_id
from backend.models.category import Category
from backend.controller.log_controller import creating_log
from backend.models.log import Log, current_date


def creating_category(ca: Category) -> None:
    create_category(ca)
    creating_log(Log(current_date(), 'create', 'category'))


def reading_categories() -> list:
    categories = read_categories()
    creating_log(Log(current_date(), 'read', 'category'))
    return categories


def updating_categories(ca: Category) -> None:
    update_categories(ca)
    creating_log(Log(current_date(), 'update', 'category'))


def deleting_categories(ca: Category) -> None:
    delete_categories(ca)
    creating_log(Log(current_date(), 'delete', 'category'))


def reading_categories_by_id(id: int):
    categories = read_categories_by_id(id)
    creating_log(Log(current_date(), 'read_by_id', 'category'))
    return categories
