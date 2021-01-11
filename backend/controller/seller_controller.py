from ..dao_txt.seller_dao_txt import get_seller, create_seller
from .log_controller import write_log, get_log

def creating_seller(seller) -> None:
    create_seller(seller)
    write_log(action='register', type='seller')

def list_sellers() -> list:
    sellers = get_seller()
    write_log(action="list",type="sellers")
    return sellers