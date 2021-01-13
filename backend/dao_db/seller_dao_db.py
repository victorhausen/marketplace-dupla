import sys

sys.path.append('.')

from backend.dao_db.connection import db_connection
from backend.controller.log_controller import write_log
from backend.models.seller import Seller
from backend.models.log import Log, current_date


def create_seller(seller: Seller) -> None:
    db = db_connection()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO seller(name, email, phone) values('{seller.name}','{seller.email}','{seller.phone}');")
    db.commit()
    cursor.close()
    db.close()
    write_log(Log(current_date(), 'create', 'seller'))


def get_sellers() -> list:
    sellers = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT name, email, phone, id FROM seller;")
    list_sellers = cursor.fetchall()

    for sel in list_sellers:
        result = Seller(sel[0], sel[2], sel[1])
        sellers.append(result)

    cursor.close()
    db.close()
    write_log(Log(current_date(), 'list', 'seller'))
    return sellers;

