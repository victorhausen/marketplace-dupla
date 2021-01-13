from backend.dao_db.connection import db_connection
from backend.models.seller import Seller


def create_seller(seller: Seller) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO seller(name, email, phone) values('{seller.name}','{seller.email}','{seller.phone}');")
        db.commit()


def read_sellers() -> list:
    sellers = []
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT name, email, phone, id FROM seller;")
        list_sellers = cursor.fetchall()
        for sel in list_sellers:
            result = Seller(sel[0], sel[2], sel[1])
            sellers.append(result)
    return sellers;
