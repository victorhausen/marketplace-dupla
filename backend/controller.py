import json
class Controller:

    def __init__(self, path):
        self.path = path
    
    def create(self, data)-> None:
        self.arquivo = open(self.path, 'a')

        self.arquivo.write(str(data)+"\n")

        self.arquivo.close()


    def get_marketplace(self) -> None:
        list_marketplace = []
        self.arquivo = open(self.path, 'r')
        for a in self.arquivo:
            b = json.loads(a.replace("'", '"'))
            mrktplace = {
                'name': b['name'],
                'description': b['description']
            }
            list_marketplace.append(mrktplace)
        return list_marketplace
    
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


    def get_categories(self)-> None:
        list_categories = []
        self.arquivo = open(self.path, 'r')
        for a in self.arquivo:
            categoria = json.loads(a.replace("'", '"'))
            categories = {
                'name': categoria['name'],
                'description': categoria['description']
            }
            list_categories.append(categories)
        return list_categories
      
    def get_seller(self)-> None:
        list_seller = []
        self.arquivo = open(self.path, 'r')
        for a in self.arquivo:
            intermediario = json.loads(a.replace("'", '"'))
            product = {
                'full_name': intermediario['full_name'],
                'contact': intermediario['contact'],
                'email': intermediario['email']
            }
            list_seller.append(product)
        return list_seller
        
    def get_log(self)-> None:
        lista_log = []
        self.arquivo = open('log.txt', 'r')
        for a in self.arquivo:
            intermediario = json.loads(a.replace("'", '"'))
            product = {
                'action': intermediario['action'],
                'type': intermediario['type'],
            }
            lista_log.append(product)
        return lista_log
    

