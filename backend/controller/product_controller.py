from backend.dao_db.product_dao_db import create_product, read_products
from backend.models.product import Product
from backend.models.log import Log, current_date
from backend.controller.log_controller import creating_log


def creating_product(pr: Product) -> None:
    create_product(pr)
    creating_log(Log(current_date(), 'create', 'product'))


def reading_products() -> list:
    products = read_products()
    creating_log(Log(current_date(), 'list', 'product'))
    return products
