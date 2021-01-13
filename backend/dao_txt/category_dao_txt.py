import json
from backend.controller.log_controller import creating_log

_path = 'database/categories_database.txt'


def create_category(category) -> list:
    name = category.get('name')
    description = category.get('description')
    string = '{' + f"'name': '{name}', 'description': '{description}'" + '}\n'
    with open(_path, 'a') as arquivo:
        arquivo.write(string)
    creating_log(action='create', type='category')


def read_categories() -> list:
    list_categories = []
    with open(_path, 'r') as archive:
        for line in archive:
            categoria = json.loads(line.replace("'", '"'))
            categories = {
                'name': categoria['name'],
                'description': categoria['description']
            }
            list_categories.append(categories)
    creating_log(action='list', type='category')
    return list_categories
