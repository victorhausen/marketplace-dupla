from backend.dao_db.marketplace_dao_db import create_marketplace, read_marketplaces
from backend.models.marketplace import Marketplace
from backend.models.log import Log, current_date
from backend.controller.log_controller import creating_log


def creating_marketplace(mp: Marketplace) -> None:
    create_marketplace(mp)
    creating_log(Log(current_date(), 'create', 'marketplace'))


def reading_marketplaces() -> list:
    marketplaces = read_marketplaces()
    creating_log(Log(current_date(), 'list', 'marketplace'))
    return marketplaces
