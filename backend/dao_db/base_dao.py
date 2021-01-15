from .connection import Connection


class BaseDao:
    def execute(self, query: str) -> None:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

    def read(self, query: str) -> tuple:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        return result
