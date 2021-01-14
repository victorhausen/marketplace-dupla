from backend.dao_db.connection import db_connection
from backend.models.category import Category


def create_category(ca: Category) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO category (name, description) values('{ca.name}', '{ca.description}');")
        db.commit()


def read_categories() -> list:
    categories = []
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM category;")
        list_categories = cursor.fetchall()
        for category in list_categories:
            result = Category(category[1], category[2], category[0])
            categories.append(result)
    return categories


def update_categories(ca: Category):
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"""
                        UPDATE category
                        SET name='{ca.name}', description='{ca.description}'
                        WHERE id={ca.id};
                        """)
        db.commit()


def delete_categories(id: int):
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"""
                        DELETE FROM category
                        WHERE id={id};
                        """)
        db.commit()


def read_categories_by_id(id: int) -> Category:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM category WHERE id={id};")
        categories = cursor.fetchall()

        ca = Category(categories[0][1], categories[0][2], categories[0][0])

    return ca
