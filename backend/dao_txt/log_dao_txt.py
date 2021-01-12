import json
from datetime import datetime
from .log_controller import write_log

_log_path = "database/log_database.txt"

def current_date() -> str:
    data_atual = datetime.now()
    data_completa = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_completa

def generate_log(action, type):
    with open(_log_path, "a") as file_:
        data = {
            'date': current_date(),
            'action': action,
            'type': type
        }
        file_.write(str(data)+"\n")

def list_logs()-> list:
    lista_log = []
    with open(_log_path, 'r') as file_:
        for a in file_:
            intermediario = json.loads(a.replace("'", '"'))
            logs = {
                'date': intermediario['date'],
                'action': intermediario['action'],
                'type': intermediario['type'],
            }
            lista_log.append(logs)
    write_log(action="list",type="log")
    return lista_log
