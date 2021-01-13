import json
from backend.controller.log_controller import creating_log

_product_path = "database/product_database.txt"


def create_product(name, description, price) -> None:
    with open(_product_path, 'a') as file_:
        product = f"{{'name': '{name}', 'description': '{description}', 'price': '{price}'}}\n"
        file_.write(product)
    creating_log(action="create", type="product")


def read_products() -> list:
    lista_products = []
    with open(_product_path, 'r') as file_:
        for a in file_:
            intermediario = json.loads(a.replace("'", '"'))
            product = {
                'name': intermediario['name'],
                'description': intermediario['description'],
                'price': intermediario['price']
            }
            lista_products.append(product)
    creating_log(action="list", type="products")
    return lista_products
