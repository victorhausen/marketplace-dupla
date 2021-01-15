from backend.dao_db.connection import Connection
from backend.models.category import Category


def create_category(category: Category) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        INSERT INTO category 
                        (name, description) 
                        values('{category.name}', '{category.description}');
                        """)
        conn.commit()


def read_categories() -> list:
    categories = []
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category;")
        list_categories = cursor.fetchall()
        for category in list_categories:
            result = Category(category[1], category[2], category[0])
            categories.append(result)

    return categories


def update_categories(category: Category):
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        UPDATE category
                        SET name='{category.name}', description='{category.description}'
                        WHERE id={category.id};
                        """)
        conn.commit()


def delete_categories(id: int):
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        DELETE FROM category
                        WHERE id={id};
                        """)
        conn.commit()


def read_categories_by_id(id: int) -> Category:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM category WHERE id={id};")
        categories = cursor.fetchall()

        results = Category(categories[0][1], categories[0][2], categories[0][0])

    return results
