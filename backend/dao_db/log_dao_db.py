from backend.dao_db.connection import Connection
from backend.models.log import Log, format_date_to_print


def create_log(log: Log) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        INSERT INTO log 
                        (date, description) 
                        values('{log.date}', '{log.action} {log.type_}');
                        """)
        conn.commit()


def read_logs() -> list:
    lista_logs = []
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM log")
        logs = cursor.fetchall()
        for log in logs:
            description = log[2].split(' ')
            result = Log(format_date_to_print(log[1]), description[0], description[1])
            lista_logs.append(result)

    return lista_logs


