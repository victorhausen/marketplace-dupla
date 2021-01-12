import psycopg2
from .log_controller import write_log
from .connection import db_connection

def create_marketplace(name, description)-> None:
    db = db_connection()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO marketplace (name, description) values('{name}', '{description}');")
    db.commit()
    cursor.close()
    db.close()
    write_log(action="create",type="marketplace")

def get_marketplaces() -> list:
    list_marketplaces = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM marketplace")
    marketplaces = cursor.fetchall()
    for marketplace in marketplaces:
        result = {'name': marketplace[1],
            'description': marketplace[2]
            }
        list_marketplaces.append(result)
    cursor.close()
    db.close()
    write_log(action='list', type='marketplace')
    return list_marketplaces