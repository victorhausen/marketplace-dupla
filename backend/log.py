from datetime import datetime

def retorna_data():
    data_atual = datetime.now()

    data_completa = data_atual.strftime("%d/%m/%Y %H:%M:%S")

    return data_completa

def write_log(action, type):
    file = open("log.txt", "a")
    data = {
        'action': action,
        'type': type
    }
    file.write(str(data)+"\n")
    file.close()
    # "create marketplace [%d/%m/%Y %H:%M:%S]"
