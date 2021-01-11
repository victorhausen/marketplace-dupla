import json
from datetime import datetime

_log_path = "database/log_database.txt"

def generate_log(action, type):
    file = open(_log_path, "a")
    data = {
        'action': action,
        'type': type
    }
    file.write(str(data)+"\n")
    file.close()

def list_logs()-> None:
        lista_log = []
        arquivo = open(_log_path, 'r')
        for a in arquivo:
            intermediario = json.loads(a.replace("'", '"'))
            produto = {
                'action': intermediario['action'],
                'type': intermediario['type'],
            }
            lista_log.append(produto)
        return lista_log
