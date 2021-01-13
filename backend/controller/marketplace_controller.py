from backend.dao_db.marketplace_dao_db import create_marketplace, get_marketplaces
from backend.models.marketplace import Marketplace


def creating_marketplace(mp: Marketplace) -> None:
    create_marketplace(mp)


def list_marketplaces() -> list:
    marketplaces = get_marketplaces()
    return marketplaces
