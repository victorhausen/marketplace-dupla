import json

_path = 'backend/database/categories_database.txt'

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