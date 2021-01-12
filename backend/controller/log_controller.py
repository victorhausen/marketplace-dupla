from ..dao_db.log_dao_db import generate_log, list_logs

def write_log(action, type)-> None:
        generate_log(action, type)

def get_log() -> list:
        logs = list_logs()
        return logs