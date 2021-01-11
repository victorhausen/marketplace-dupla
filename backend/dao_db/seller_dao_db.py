from .connection import db

def create_seller_db(seller) -> None:
    cursor = db.cursor()
    name = seller.get('full_name')
    email = seller.get('seller_email')
    phone = seller.get('contact_number')
    values = (name, email, phone)
    cursor.execute("INSERT INTO seller(name, email, phone) values(%s, %s, %s);", values)

    db.commit()
    cursor.close()

def get_sellers_db() -> list:
    sellers = []
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
    return sellers;