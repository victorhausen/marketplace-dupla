from ..dao_txt.seller_dao_txt import get_seller, create_seller

def creating_seller(seller) -> None:
    create_seller(seller)

def list_sellers() -> list:
    sellers = get_seller()
    return sellers