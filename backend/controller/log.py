from datetime import datetime

_log_path = "database/log_database.txt"

def retorna_data():
    data_atual = datetime.now()
    data_completa = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_completa

def write_log(action, type):
    file = open(_log_path, "a")
    data = {
        'action': action,
        'type': type
    }
    file.write(str(data)+"\n")
    file.close()

def get_log(self)-> None:
        lista_log = []
        self.arquivo = open(_log_path, 'r')
        for a in self.arquivo:
            intermediario = json.loads(a.replace("'", '"'))
            produto = {
                'action': intermediario['action'],
                'type': intermediario['type'],
            }
            lista_log.append(produto)

        return lista_log
