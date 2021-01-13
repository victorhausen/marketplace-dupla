from backend.dao_db.log_dao_db import create_log, read_logs
from backend.models.log import Log


def creating_log(log: Log) -> None:
    create_log(log)

    
def reading_log() -> list:
    logs = read_logs()
    return logs
