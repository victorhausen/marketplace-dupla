from backend.models.product import Product
from backend.dao_db.base_dao import BaseDao

class ProductDao(BaseDao):
    def create(self, product: Product) -> None:
        query = f"""
                INSERT INTO product 
                (name, description, price) 
                values('{product.name}', '{product.description}', {product.price});
                """
        super().execute(query)

    def read_all(self) -> list:
        list_products = []
        query = "SELECT name, description, price, id FROM product"
        products = super().read(query)
        for prod in products:
            result = Product(prod[0], prod[1], prod[2], prod[3])
            list_products.append(result)
        return list_products

    def update(self, product: Product) -> None:
        query = f"""
                UPDATE product 
                SET name='{product.name}', description='{product.description}', price={product.price} 
                WHERE id={product.id};
                """
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"""
                DELETE FROM product
                WHERE id={id};
                """
        super().execute(query)

    def read_by_id(self, id: int) -> Product:
        query = f"SELECT name, description, price, id FROM product WHERE id={id};"
        prod = super().read(query)[0]
        results = Product(prod[0], prod[1], prod[2].replace("$", ""), prod[3])
        return results

