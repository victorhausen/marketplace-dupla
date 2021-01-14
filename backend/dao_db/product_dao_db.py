from backend.dao_db.connection import db_connection
from backend.models.product import Product


def create_product(pr: Product) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(
            f"INSERT INTO product (name, description, price) values('{pr.name}', '{pr.description}', {pr.price});")
        db.commit()


def read_products() -> list:
    lista_products = []
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        for product in products:
            result = Product(product[1], product[2], product[3], product[0])
            lista_products.append(result)
    return lista_products


def update_product(pr: Product):
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"""
                            UPDATE product 
                            SET name='{pr.name}', description='{pr.description}', price={pr.price} 
                            WHERE id={pr.id};
                        """)
        db.commit()


def delete_product(id: int):
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"""
                        DELETE FROM product
                        WHERE id={id};
                        """)
        db.commit()


def read_product_by_id(id: int) -> Product:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE id={id};")
        products = cursor.fetchall()

        pr = Product(products[0][1], products[0][2], products[0][3], products[0][0])

    return pr


