from ..dao_txt.seller_dao_txt import get_seller, create_seller
from ..dao_db.seller_dao_db import get_sellers_db, create_seller_db

def creating_seller(seller) -> None:
    create_seller(seller)

def list_sellers() -> list:
    sellers = get_seller()
    return sellers

def creating_seller_db(seller) -> None:
    create_seller_db(seller)

def list_sellers_db() -> list:
    sellers = get_sellers_db()
    print(sellers[0])
    return sellers