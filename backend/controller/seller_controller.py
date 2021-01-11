from ..dao_txt.seller_dao_txt import get_seller
    
def list_sellers() -> list:
    sellers = get_seller()
    return sellers