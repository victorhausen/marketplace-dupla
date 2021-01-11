import json
from ..controller.log_controller import write_log

_path = 'database/categories_database.txt'

def create_category(category) -> list:
    name = category.get('name')
    description = category.get('description')
    string = '{' + f"'name': '{name}', 'description': '{description}'" + '}\n'
    arquivo = open(_path, 'a')
    arquivo.write(string)
    arquivo.close()
    write_log(action='create', type='category')

def get_categories() -> list:
    list_categories = []
    archive = open(_path, 'r')
    for line in archive:
        categoria = json.loads(line.replace("'", '"'))
        categories = {
            'name': categoria['name'],
            'description': categoria['description']
        }
        list_categories.append(categories)
    write_log(action='list', type='category')
    return list_categories