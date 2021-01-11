from ..dao_txt.product_dao_txt import create_product, get_products

def creating_product(name, description, price)-> None:
        create_product(name, description, price)

def list_products() -> None:
        products = get_products()
        return products