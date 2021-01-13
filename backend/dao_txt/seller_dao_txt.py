import json
from ..controller.log_controller import creating_log

_path = 'database/seller_database.txt'


def create_seller(seller) -> list:
    name = seller.get('full_name')
    email = seller.get('seller_email')
    phone = seller.get('contact_number')
    string = '{' + f"'full_name': '{name}', 'contact': '{email}', 'email': '{phone}'" + '}\n'
    with open(_path, 'a') as arquivo:
        arquivo.write(string)
    creating_log(action='create', type='seller')


def read_seller() -> list:
    list_seller = []
    with open(_path, 'r') as archive:
        for line in archive:
            intermediario = json.loads(line.replace("'", '"'))
            seller = {
                'full_name': intermediario['full_name'],
                'contact': intermediario['contact'],
                'email': intermediario['email']
            }
            list_seller.append(seller)
    creating_log(action='list', type='seller')
    return list_seller
