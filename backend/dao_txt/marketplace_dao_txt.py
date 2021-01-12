import json
from .log_controller import write_log

_marketplace_path = "database/marketplace_database.txt"

def create_marketplace(name, description)-> None:
        with open(_marketplace_path, 'a') as file_:
            marketplace = f"{{'name': '{name}', 'description': '{description}'}}\n"
            file_.write(marketplace)
        write_log(action="create",type="marketplace")

def get_marketplaces() -> list:
    list_marketplaces = []
    with open(_marketplace_path, 'r') as file_:
        for a in file_:
            b = json.loads(a.replace("'", '"'))
            mrktplace = {
                'name': b['name'],
                'description': b['description']
            }
            list_marketplaces.append(mrktplace)
    write_log(action='list', type='marketplace')
    return list_marketplaces