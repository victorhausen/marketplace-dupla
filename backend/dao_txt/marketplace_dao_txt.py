import json

_marketplace_path = "database/marketplace_database.txt"

def create_marketplace(name, description)-> None:
        with open(_marketplace_path, 'a') as file_:
            marketplace = f"{{'name': '{name}', 'description': '{description}'}}\n"
            file_.write(marketplace)

def get_marketplaces() -> None:
        list_marketplaces = []
        with open(_marketplace_path, 'r') as file_:
            for a in file_:
                b = json.loads(a.replace("'", '"'))
                mrktplace = {
                    'name': b['name'],
                    'description': b['description']
                }
                list_marketplaces.append(mrktplace)
        return list_marketplaces