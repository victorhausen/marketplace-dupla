from backend.dao_db.seller_dao_db import read_sellers, create_seller, update_seller, delete_seller, read_seller_by_id
from backend.models.log import Log, current_date
from backend.controller.log_controller import creating_log
from backend.models.seller import Seller


def creating_seller(seller: Seller) -> None:
    create_seller(seller)
    creating_log(Log(current_date(), 'create', 'seller'))


def reading_sellers() -> list:
    sellers = read_sellers()
    creating_log(Log(current_date(), 'read', 'seller'))
    return sellers


def updating_seller(seller: Seller) -> None:
    update_seller(seller)
    creating_log(Log(current_date(), 'update', 'seller'))


def deleting_seller(id: int) -> None:
    delete_seller(id)
    creating_log(Log(current_date(), 'delete', 'seller'))


def reading_seller_by_id(id: int) -> Seller:
    seller = read_seller_by_id(id)
    creating_log(Log(current_date(), 'read_by_id', 'seller'))
    return seller
