from backend.dao_db.product_dao_db import create_product, get_products
from backend.models.product import Product


def creating_product(pr: Product) -> None:
    create_product(pr)


def list_products() -> list:
    products = get_products()
    return products
