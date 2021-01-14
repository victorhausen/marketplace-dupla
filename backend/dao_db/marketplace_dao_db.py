from backend.dao_db.connection import Connection
from backend.models.marketplace import Marketplace


def create_marketplace(marketplace: Marketplace) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        INSERT INTO marketplace 
                        (name, description) 
                        values('{marketplace.name}', '{marketplace.description}');""")
    conn.commit()


def read_marketplaces() -> list:
    list_marketplaces = []
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM marketplace")
        marketplaces = cursor.fetchall()
        for mp in marketplaces:
            result = Marketplace(mp[1], mp[2], mp[0])
            list_marketplaces.append(result)

    return list_marketplaces


def update_marketplace(marketplace: Marketplace) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        UPDATE marketplace 
                        SET name='{marketplace.name}', description='{marketplace.description}'
                        WHERE id={marketplace.id};
                        """)
    conn.commit()


def delete_marketplace(id: int) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        DELETE FROM marketplace
                        WHERE id={id};
                        """)
    conn.commit()


def read_marketplace_by_id(id: int) -> Marketplace:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM marketplace where id ={id}")
        marketplace = cursor.fetchall()
        results = Marketplace(marketplace[0][1], marketplace[0][2], marketplace[0][0])

    return results
