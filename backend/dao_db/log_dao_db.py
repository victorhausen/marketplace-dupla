from backend.models.log import Log
from backend.dao_db.base_dao import BaseDao


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)



