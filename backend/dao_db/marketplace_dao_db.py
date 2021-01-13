from backend.controller.log_controller import creating_log
from backend.dao_db.connection import db_connection
from backend.models.marketplace import Marketplace
from backend.models.log import Log, current_date


def create_marketplace(mp: Marketplace) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO marketplace (name, description) values('{mp.name}', '{mp.description}');")
    db.commit()
    creating_log(Log(current_date(), 'create', 'marketplace'))


def read_marketplaces() -> list:
    list_marketplaces = []
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM marketplace")
        marketplaces = cursor.fetchall()
        for mp in marketplaces:
            result = Marketplace(mp[1], mp[2], mp[0])
            list_marketplaces.append(result)
    creating_log(Log(current_date(), 'list', 'marketplace'))
    return list_marketplaces
