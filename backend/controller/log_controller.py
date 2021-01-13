from backend.dao_db.log_dao_db import generate_log, list_logs
from backend.models.log import Log


def write_log(log: Log) -> None:
    generate_log(log)


def get_log() -> list:
    logs = list_logs()
    return logs
