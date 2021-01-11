import json

_product_path = "database/product_database.txt"

def create_product(name, description, price)-> None:
        with open(_product_path, 'a') as file_:
            product = f"{{'name': '{name}', 'description': '{description}', 'price': '{price}'}}\n"
            file_.write(product)

def get_products()-> None:
        lista_product = []
        with open(_product_path, 'r') as file_:
            for a in file_:
                intermediario = json.loads(a.replace("'", '"'))
                product = {
                    'name': intermediario['name'],
                    'description': intermediario['description'],
                    'price': intermediario['price']
                }
                lista_product.append(product)
        return lista_product