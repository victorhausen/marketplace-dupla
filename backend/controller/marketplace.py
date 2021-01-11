import json

_marketplace_path = "database/marketplace_database.txt"

def create_marketplace(data)-> None:
        arquivo = open(_marketplace_path, 'a')
        arquivo.write(str(data)+"\n")
        arquivo.close()

def get_marketplaces(self) -> None:
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