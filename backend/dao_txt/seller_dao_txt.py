import json

_path = 'backend/database/categories_database.txt'

def get_seller() -> list:
    list_seller = []
    archive = open(_path, 'r')
    for line in archive:
        intermediario = json.loads(line.replace("'", '"'))
        product = {
            'full_name': intermediario['full_name'],
            'contact': intermediario['contact'],
            'email': intermediario['email']
        }
        list_seller.append(product)
    return list_seller