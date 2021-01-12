import sys

sys.path.append('.')

from backend.controller.log_controller import write_log
from backend.dao_db.connection import db_connection
from backend.models.log import Log, current_date


def create_product(name, description, price) -> None:
    db = db_connection()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO product (name, description, price) values('{name}', '{description}', '{price}');")
    db.commit()
    cursor.close()
    db.close()
    write_log(Log(current_date(), 'create', 'product'))


def get_products() -> list:
    lista_products = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        result = {'name': product[1],
                  'description': product[2],
                  'price': product[3]
                  }
        lista_products.append(result)
    cursor.close()
    db.close()
    write_log(Log(current_date(), 'list', 'product'))
    return lista_products
