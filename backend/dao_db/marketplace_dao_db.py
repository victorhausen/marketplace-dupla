from backend.dao_db.connection import db_connection
from backend.models.marketplace import Marketplace



def create_marketplace(mp: Marketplace) -> None:
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO marketplace (name, description) values('{mp.name}', '{mp.description}');")
    db.commit()



def read_marketplaces() -> list:
    list_marketplaces = []
    with db_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM marketplace")
        marketplaces = cursor.fetchall()
        for mp in marketplaces:
            result = Marketplace(mp[1], mp[2], mp[0])
            list_marketplaces.append(result)
    return list_marketplaces
