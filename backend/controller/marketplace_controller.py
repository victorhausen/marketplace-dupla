from ..dao_txt.marketplace_dao_txt import create_marketplace, get_marketplaces

def creating_marketplace(marketplace)-> None:
        create_marketplace(marketplace)

def list_marketplaces() -> None:
        marketplaces = get_marketplaces()
        return marketplaces