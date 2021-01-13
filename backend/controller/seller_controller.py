from backend.dao_db.seller_dao_db import read_sellers, create_seller
from backend.models.log import Log, current_date
from backend.controller.log_controller import creating_log


def creating_seller(seller) -> None:
    create_seller(seller)
    creating_log(Log(current_date(), 'create', 'seller'))


def reading_sellers() -> list:
    sellers = read_sellers()
    creating_log(Log(current_date(), 'list', 'seller'))
    return sellers
