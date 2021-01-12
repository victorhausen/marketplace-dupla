from ..dao_db.marketplace_dao_db import create_marketplace, get_marketplaces

def creating_marketplace(name, description)-> None:
        create_marketplace(name, description)

def list_marketplaces() -> list:
        marketplaces = get_marketplaces()
        return marketplaces