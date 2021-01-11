import psycopg2

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills3'
_password = 'olist21'
_database = 'topskills3'
_connection_string = f'host={_host} user={_user} dbname={_database} password={_password}'

def create_product(name, description, price)-> None:
    conn = psycopg2.connect(_connection_string)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO product (name, description, price) values('{name}', '{description}', '{price}');")
    conn.commit()
    cur.close()
    conn.close()

def get_products() -> None:
        lista_products = []
        conn = psycopg2.connect(_connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        for product in products:
            result = {'name': product[1],
                'description': product[2],
                'price': product[3]
                }
            lista_products.append(result)
        cursor.close()
        conn.close()
        return lista_products