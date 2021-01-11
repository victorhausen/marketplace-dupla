from .connection import db_connection
from ..controller.log_controller import write_log

def create_seller_db(seller) -> None:
    db = db_connection()
    cursor = db.cursor()
    name = seller.get('full_name')
    email = seller.get('seller_email')
    phone = seller.get('contact_number')
    values = (name, email, phone)
    cursor.execute("INSERT INTO seller(name, email, phone) values(%s, %s, %s);", values)

    db.commit()
    cursor.close()
    db.close()
    write_log(action='create', type='seller')

def get_sellers_db() -> list:
    sellers = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT name, email, phone FROM seller;")
    list_sellers = cursor.fetchall()

    for tupla in list_sellers:
        seller = {
            'full_name': tupla[0],
            'contact': tupla[1],
            'email': tupla[2]
        }
        sellers.append(seller)

    cursor.close()
    db.close()
    write_log(action='list', type='seller')
    return sellers;