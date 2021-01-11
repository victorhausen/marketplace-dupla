import psycopg2

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills3'
_password = 'olist21'
_database = 'topskills3'
_connection_string = f'host={_host} user={_user} dbname={_database} password={_password}'

def create_marketplace(name, description)-> None:
    conn = psycopg2.connect(_connection_string)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO marketplace (name, description) values('{name}', '{description}');")
    conn.commit()
    cur.close()
    conn.close()

def get_marketplaces() -> None:
        list_marketplaces = []
        conn = psycopg2.connect(_connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM marketplace")
        marketplaces = cursor.fetchall()
        for marketplace in marketplaces:
            result = {'name': marketplace[1],
                'description': marketplace[2]
                }
            list_marketplaces.append(result)
        cursor.close()
        conn.close()
        return list_marketplaces