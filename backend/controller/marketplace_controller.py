from backend.dao_db.marketplace_dao_db import create_marketplace, read_marketplaces
from backend.models.marketplace import Marketplace


def creating_marketplace(mp: Marketplace) -> None:
    create_marketplace(mp)


def reading_marketplaces() -> list:
    marketplaces = read_marketplaces()
    return marketplaces
