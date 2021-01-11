from ..dao_txt.log_dao_txt import generate_log, list_logs

def write_log(action, type)-> None:
        generate_log(action, type)

def get_log() -> None:
        logs = list_logs()
        return logs