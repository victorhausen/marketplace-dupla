import json

_product_path = "database/product_database.txt"

def create_product(data)-> None:
        arquivo = open(_product_path, 'a')
        arquivo.write(str(data)+"\n")
        arquivo.close()

def get_products(self)-> None:
        lista_product = []
        self.arquivo = open(self.path, 'r')
        for a in self.arquivo:
            intermediario = json.loads(a.replace("'", '"'))
            product = {
                'name': intermediario['name'],
                'description': intermediario['description'],
                'price': intermediario['price']
            }
            lista_product.append(product)
        return lista_product