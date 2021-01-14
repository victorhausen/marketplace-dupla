import psycopg2


class Connection:
    def __get_connection_string(self):
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills3'
        database = 'topskills3'
        password = 'olist21'
        connection_string = f'host={host} user={user} dbname={database} password={password}'
        return connection_string

    def __enter__(self):
        self.__connection = psycopg2.connect(self.__get_connection_string())
        return self.__connection

    def __exit__(self, type, value, trace):
        self.__connection.close()
