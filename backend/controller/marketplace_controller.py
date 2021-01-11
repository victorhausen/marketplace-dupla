from ..dao_txt.marketplace_dao_txt import create_marketplace, get_marketplaces

def creating_marketplace(name, description)-> None:
        create_marketplace(name, description)

def list_marketplaces() -> None:
        marketplaces = get_marketplaces()
        return marketplaces