from .connection import db_connection

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
    return categories;