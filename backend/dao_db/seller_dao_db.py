from backend.dao_db.connection import db_connection
from backend.models.seller import Seller


def create_seller(seller: Seller) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(
            f"INSERT INTO seller(name, email, phone) values('{seller.name}','{seller.email}','{seller.phone}');")
        db.commit()


def read_sellers() -> list:
    sellers = []
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT name, phone, email,  id FROM seller;")
        list_sellers = cursor.fetchall()
        for sel in list_sellers:
            result = Seller(sel[0], sel[1], sel[2], sel[3])
            sellers.append(result)
    return sellers


def update_seller(seller: Seller) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(
            f"""
                update seller 
                set name='{seller.name}', email='{seller.email}', phone='{seller.phone}'
                where id={seller.id};
            """
        )
    db.commit()


def delete_seller(id: int) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(
            f"""
                delete from seller
                where id={id};
            """
        )
    db.commit()


def read_seller_by_id(id: int) -> Seller:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT name, phone, email, id FROM seller where id ={id}")
        seller = cursor.fetchall()
        sel = Seller(seller[0][0], seller[0][1], seller[0][2], seller[0][3])
    return sel