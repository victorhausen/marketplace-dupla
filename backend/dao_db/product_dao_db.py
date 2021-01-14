from backend.dao_db.connection import Connection
from backend.models.product import Product


def create_product(product: Product) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        INSERT INTO product 
                        (name, description, price) 
                        values('{product.name}', '{product.description}', {product.price});
                        """)
        conn.commit()


def read_products() -> list:
    lista_products = []
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        for product in products:
            result = Product(product[1], product[2], product[3], product[0])
            lista_products.append(result)

    return lista_products


def update_product(product: Product):
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        UPDATE product 
                        SET name='{product.name}', description='{product.description}', price={product.price} 
                        WHERE id={product.id};
                        """)
        conn.commit()


def delete_product(id: int):
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
                        DELETE FROM product
                        WHERE id={id};
                        """)
        conn.commit()


def read_product_by_id(id: int) -> Product:
    with Connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM product WHERE id={id};")
        products = cursor.fetchall()

        results = Product(products[0][1], products[0][2], products[0][3], products[0][0])

    return results


