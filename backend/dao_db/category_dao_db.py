from backend.dao_db.connection import db_connection
from backend.controller.log_controller import write_log
from backend.models.category import Category


def create_category(ca: Category) -> None:
    db = db_connection()
    cursor = db.cursor()
    # name = ca.get('name')
    # description = ca.get('description')
    # values = (name, description)
    cursor.execute(f"INSERT INTO category (name, description) values('{ca.name}', '{ca.description}');")
    db.commit()
    cursor.close()
    db.close()
    write_log(action='create', type='category')


def get_categories() -> list:
    categories = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM category")
    list_categories = cursor.fetchall()

    for category in list_categories:
        result = Category(category[1], category[2], category[0])
        categories.append(result)

    cursor.close()
    db.close()
    write_log(action='list', type='category')
    return categories
