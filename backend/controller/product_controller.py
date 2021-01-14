from backend.dao_db.product_dao_db import create_product, read_products, update_product, delete_product, read_product_by_id
from backend.models.product import Product
from backend.models.log import Log, current_date
from backend.controller.log_controller import creating_log


def creating_product(pr: Product) -> None:
    create_product(pr)
    creating_log(Log(current_date(), 'create', 'product'))


def reading_products() -> list:
    products = read_products()
    creating_log(Log(current_date(), 'read', 'product'))
    return products


def updating_products(pr: Product) -> None:
    update_product(pr)
    creating_log(Log(current_date(), 'update', 'product'))


def deleting_product(id: int) -> None:
    delete_product(id)
    creating_log(Log(current_date(), 'delete', 'product'))


def reading_product_by_id(id: int):
    products = read_product_by_id(id)
    creating_log(Log(current_date(), 'read_by_id', 'product'))
    return products
