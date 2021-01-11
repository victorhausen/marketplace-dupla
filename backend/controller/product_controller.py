from ..dao_txt.product_dao_txt import create_product, get_products

def creating_product(product)-> None:
        create_product(product)

def list_products() -> None:
        products = get_products()
        return products