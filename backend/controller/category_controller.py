from ..dao_txt.category_dao_txt import get_categories, create_category
from .log_controller import write_log, get_log

def creating_category(category) -> None:
    create_category(category)
    write_log(action="create", type="category")

def list_categories() -> list:
    categories = get_categories()
    write_log(action="list", type="categories")
    return categories