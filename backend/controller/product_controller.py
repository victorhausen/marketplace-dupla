from backend.dao_db.product_dao_db import create_product, read_products
from backend.models.product import Product


def creating_product(pr: Product) -> None:
    create_product(pr)


def reading_products() -> list:
    products = read_products()
    return products
