import sys
sys.path.append('.')

from backend.dao_db.connection import db_connection
from backend.controller.log_controller import write_log
from backend.models.log import Log, current_date


def create_category(category) -> None:
    db = db_connection()
    cursor = db.cursor()
    name = category.get('name')
    description = category.get('description')
    values = (name, description)
    cursor.execute("INSERT INTO category(name, description) values(%s, %s);", values)
    db.commit()
    cursor.close()
    db.close()
    write_log(Log(current_date(), 'create', 'category'))


def get_categories() -> list:
    categories = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT name, description FROM category;")
    list_categories = cursor.fetchall()

    for tupla in list_categories:
        category = {
            'name': tupla[0],
            'description': tupla[1]
        }
        categories.append(category)

    cursor.close()
    db.close()
    write_log(Log(current_date(), 'list', 'category'))
    return categories;