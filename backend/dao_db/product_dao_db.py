import psycopg2
from backend.controller.log_controller import write_log
from backend.dao_db.connection import db_connection
from backend.models.product import Product


def create_product(pr: Product) -> None:
    db = db_connection()
    cursor = db.cursor()
    cursor.execute(
        f"INSERT INTO product (name, description, price) values('{pr.name}', '{pr.description}', {pr.price});")
    db.commit()
    cursor.close()
    db.close()
    write_log(action="create", type="product")


def get_products() -> list:
    lista_products = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        result = Product(product[1], product[2], product[3], product[0])
        lista_products.append(result)
    cursor.close()
    db.close()
    write_log(action="list", type="products")
    return lista_products
