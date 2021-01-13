from backend.dao_db.connection import db_connection
from backend.controller.log_controller import creating_log
from backend.models.category import Category
from backend.models.log import Log, current_date


def create_category(ca: Category) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO category (name, description) values('{ca.name}', '{ca.description}');")
        db.commit()
    creating_log(Log(current_date(), 'create', 'category'))


def read_categories() -> list:
    categories = []
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM category")
        list_categories = cursor.fetchall()
        for category in list_categories:
            result = Category(category[1], category[2], category[0])
            categories.append(result)
    creating_log(Log(current_date(), 'list', 'category'))
    return categories
