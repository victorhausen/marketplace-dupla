import json

_path = 'database/seller_database.txt'

def create_seller(seller) -> list:
    name = seller.get('full_name')
    email = seller.get('email')
    phone = seller.get('contact')
    string = '{' + f"'full_name': '{name}', 'contact': '{email}', 'email': '{phone}'" + '}\n'
    arquivo = open(_path, 'a')
    arquivo.write(string)
    arquivo.close()

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