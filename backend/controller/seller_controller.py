from backend.dao_db.seller_dao_db import read_sellers, create_seller


def creating_seller(seller) -> None:
    create_seller(seller)


def reading_sellers() -> list:
    sellers = read_sellers()
    return sellers
