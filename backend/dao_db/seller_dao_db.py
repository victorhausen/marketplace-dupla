from backend.dao_db.connection import Connection
from backend.models.seller import Seller


def create_seller(seller: Seller) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        INSERT INTO seller
                        (name, email, phone) 
                        values('{seller.name}','{seller.email}','{seller.phone}');
                        """)
        conn.commit()


def read_sellers() -> list:
    sellers = []
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone, email,  id FROM seller;")
        list_sellers = cursor.fetchall()
        for sel in list_sellers:
            result = Seller(sel[0], sel[1], sel[2], sel[3])
            sellers.append(result)

    return sellers


def update_seller(seller: Seller) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        UPDATE seller 
                        SET name='{seller.name}', email='{seller.email}', phone='{seller.phone}'
                        WHERE id={seller.id};
                        """)
    conn.commit()


def delete_seller(id: int) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        DELETE FROM seller
                        WHERE id={id};
                        """)
    conn.commit()


def read_seller_by_id(id: int) -> Seller:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, phone, email, id FROM seller WHERE id ={id}")
        seller = cursor.fetchall()
        results = Seller(seller[0][0], seller[0][1], seller[0][2], seller[0][3])

    return results
