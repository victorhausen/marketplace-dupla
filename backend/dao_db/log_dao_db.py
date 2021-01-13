import sys

sys.path.append('.')

from backend.dao_db.connection import db_connection
from backend.models.log import Log


def generate_log(log: Log) -> None:
    db = db_connection()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO log (date, description) values('{log.date}', '{log.action} {log.type_}');")
    db.commit()
    cursor.close()
    db.close()


def list_logs() -> list:
    lista_logs = []
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM log")
    logs = cursor.fetchall()
    for log in logs:
        description = log[2].split(' ')
        result = Log(log[1], description[0], description[1])
        lista_logs.append(result)
    cursor.close()
    db.close()
    return lista_logs
