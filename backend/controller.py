import json
class Controller:

    def __init__(self, path):
        self.path = path
    
    def create(self, data):
        self.arquivo = open(self.path, 'a')

        self.arquivo.write(str(data)+"\n")

        self.arquivo.close()
    def get_market(self):
        lista_market = []
        self.arquivo = open(self.path, 'r')
        for a in self.arquivo:
            json_market = json.loads(a.replace("'", '"'))
            print(json_market['name'])
            print(json_market['description'])
            market = {
                'name': json_market['name'],
                'description': json_market['description']
            }
            lista_market.append(market)
        return lista_market
    
        def get_product(self):
        lista_product = []
        self.arquivo = open(self.path, 'r')
        for a in self.arquivo:
            json_product = json.loads(a.replace("'", '"'))
            print(json_product['name'])
            print(json_product['description'])
            market = {
                'name': json_product['name'],
                'description': json_product['description'],
                'price': json_product['price']
            }
            lista_market.append(market)
        return lista_market