import json
from datetime import datetime

_log_path = "database/log_database.txt"

def generate_log(action, type):
    with open(_log_path, "a") as file_:
        data = {
            'action': action,
            'type': type
        }
        file_.write(str(data)+"\n")

def list_logs()-> None:
        lista_log = []
        with open(_log_path, 'r') as file_:
            for a in file_:
                intermediario = json.loads(a.replace("'", '"'))
                logs = {
                    'action': intermediario['action'],
                    'type': intermediario['type'],
                }
                lista_log.append(logs)
        return lista_log
