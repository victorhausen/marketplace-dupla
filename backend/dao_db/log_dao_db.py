from backend.models.log import Log
from backend.dao_db.base_dao import BaseDao


class LogDao(BaseDao):
    def create(self, log: Log) -> None:
        query = f"""
                INSERT INTO log 
                (date, description) 
                values('{log.date.strftime("%m/%d/%Y %H:%M:%S")}', '{log.action} {log.type_}');
                """
        super().execute(query)

    def read_all(self) -> list:
        list_logs = []
        query = "SELECT id, date, description FROM log"
        logs = super().read(query)
        for log in logs:
            description = log[2].split(' ')
            result = Log(format_date_to_print(log[1]), description[0], description[1])
            list_logs.append(result)
        return list_logs


def format_date_to_print(date) -> str:
    date = date.strftime("%d/%m/%Y %H:%M:%S")
    return date