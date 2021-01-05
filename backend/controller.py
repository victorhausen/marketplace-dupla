import json
class Controller:

    def __init__(self, path):
        self.path = path
    
    def create(self, data):
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
