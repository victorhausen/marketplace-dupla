import psycopg2
from datetime import datetime
from .log_controller import write_log
from .connection import db_connection

def current_date() -> str:
    data_atual = datetime.now()
    data_completa = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_completa

def generate_log(action, type_)-> None:
    db = db_connection()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO log (date, description) values('{current_date()}', '{action} {type_}');")
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
        result = {'date': log[1],
            'action': description[0],
            'type': description[1]
            }
        lista_logs.append(result)
    cursor.close()
    db.close()
    write_log(action="list",type="log")
    return lista_logs