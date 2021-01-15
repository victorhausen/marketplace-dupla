from backend.models.seller import Seller
from backend.dao_db.base_dao import BaseDao


class SellerDao(BaseDao):
    def create(self, seller: Seller) -> None:
        query = f"""
                INSERT INTO seller
                (name, email, phone) 
                values('{seller.name}','{seller.email}','{seller.phone}');
                """
        super().execute(query)

    def read_all(self) -> list:
        list_sellers = []
        query = "SELECT name, phone, email,  id FROM seller;"
        sellers = super().read(query)
        for sel in sellers:
            result = Seller(sel[0], sel[1], sel[2], sel[3])
            list_sellers.append(result)
        return list_sellers

    def update(self, seller: Seller) -> None:
        query = f"""
                UPDATE seller 
                SET name='{seller.name}', email='{seller.email}', phone='{seller.phone}'
                WHERE id={seller.id};
                """
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"""
                DELETE FROM seller
                WHERE id={id};
                """
        super().execute(query)

    def read_by_id(self, id: int) -> Seller:
        query = f"SELECT name, phone, email, id FROM seller WHERE id ={id}"
        seller = super().read(query)[0]
        results = Seller(seller[0], seller[1], seller[2], seller[3])
        return results
