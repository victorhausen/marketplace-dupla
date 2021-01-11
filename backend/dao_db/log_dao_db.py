import psycopg2
from datetime import datetime

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills3'
_password = 'olist21'
_database = 'topskills3'
_connection_string = f'host={_host} user={_user} dbname={_database} password={_password}'

def current_date():
    data_atual = datetime.now()
    data_completa = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_completa

def generate_log(action, type_)-> None:
    conn = psycopg2.connect(_connection_string)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO log (date, description) values('{current_date()}', '{action} {type_}');")
    conn.commit()
    cur.close()
    conn.close()

def list_logs() -> None:
        lista_logs = []
        conn = psycopg2.connect(_connection_string)
        cursor = conn.cursor()
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
        conn.close()
        return lista_logs