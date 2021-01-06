import json
class Controller:

    def __init__(self, path):
        self.path = path
    
    def create(self, data)-> None:
        self.arquivo = open(self.path, 'a')

        self.arquivo.write(str(data)+"\n")

        self.arquivo.close()
    
    def get_product(self)-> None:
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
