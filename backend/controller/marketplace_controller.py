from backend.dao_db.marketplace_dao_db import create_marketplace, read_marketplaces, update_marketplace, \
    delete_marketplace, read_marketplace_by_id
from backend.models.marketplace import Marketplace
from backend.models.log import Log, current_date
from backend.controller.log_controller import creating_log


def creating_marketplace(mp: Marketplace) -> None:
    create_marketplace(mp)
    creating_log(Log(current_date(), 'create', 'marketplace'))


def reading_marketplaces() -> list:
    marketplaces = read_marketplaces()
    creating_log(Log(current_date(), 'read', 'marketplace'))
    return marketplaces


def updating_marketplace(mp: Marketplace) -> None:
    update_marketplace(mp)
    creating_log(Log(current_date(), 'update', 'marketplace'))


def deleting_marketplace(id: int) -> None:
    delete_marketplace(id)
    creating_log(Log(current_date(), 'delete', 'marketplace'))


def reading_marketplace_by_id(id: int) -> Marketplace:
    marketplace = read_marketplace_by_id(id)
    creating_log(Log(current_date(), 'read_by_id', 'marketplace'))
    return marketplace
