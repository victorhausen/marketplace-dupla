import json
from ..controller.log_controller import write_log

_path = 'database/seller_database.txt'

def create_seller(seller) -> list:
    name = seller.get('full_name')
    email = seller.get('seller_email')
    phone = seller.get('contact_number')
    string = '{' + f"'full_name': '{name}', 'contact': '{email}', 'email': '{phone}'" + '}\n'
    arquivo = open(_path, 'a')
    arquivo.write(string)
    arquivo.close()
    write_log(action='create', type='seller')

def get_seller() -> list:
    list_seller = []
    archive = open(_path, 'r')
    for line in archive:
        intermediario = json.loads(line.replace("'", '"'))
        seller = {
            'full_name': intermediario['full_name'],
            'contact': intermediario['contact'],
            'email': intermediario['email']
        }
        list_seller.append(seller)
    write_log(action='list', type='seller')
    return list_seller