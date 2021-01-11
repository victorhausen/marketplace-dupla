from ..dao_txt.category_dao_txt import get_categories
    
def list_categories() -> list:
    categories = get_categories()
    return categories