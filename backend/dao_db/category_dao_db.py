from .connection import db_connection
from ..controller.log_controller import write_log

def create_category_db(category) -> None:
    db = db_connection()
    cursor = db.cursor()
    name = category.get('name')
    description = category.get('description')
    values = (name, description)
    cursor.execute("INSERT INTO category(name, description) values(%s, %s);", values)
    db.commit()
    cursor.close()
    db.close()
    write_log(action='create', type='category')

def get_categories_db() -> list:
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
    write_log(action='list', type='category')
    return categories;