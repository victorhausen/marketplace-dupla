import json

_path = 'database/categories_database.txt'

def create_category(category) -> list:
    name = category.get('name')
    description = category.get('description')
    string = '{' + f"'name': '{name}', 'description': '{description}'" + '}\n'
    arquivo = open(_path, 'a')
    arquivo.write(string)
    arquivo.close()

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
    return list_categories