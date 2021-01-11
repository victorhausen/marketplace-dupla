import psycopg2

host = 'pgsql08-farm15.uni5.net'
user = 'topskills3'
database = 'topskills3'
password = 'olist21'

connection_string = f'host={host} user={user} dbname={database} password={password}'
db = psycopg2.connect(connection_string)
