from backend.models.marketplace import Marketplace
from backend.dao_db.base_dao import BaseDao


class MarketplaceDao(BaseDao):
    def create(self, marketplace: Marketplace) -> None:
        query = f"""
                INSERT INTO marketplace 
                (name, description) 
                values
                ('{marketplace.name}', '{marketplace.description}');"""
        super().execute(query)

    def read_all(self) -> list:
        list_marketplaces = []
        query = "SELECT name, description, id FROM marketplace"
        marketplaces = super().read(query)
        for mp in marketplaces:
            result = Marketplace(mp[0], mp[1], mp[2])
            list_marketplaces.append(result)
        return list_marketplaces

    def update(self, marketplace: Marketplace) -> None:
        query = f"""
                UPDATE marketplace 
                SET name='{marketplace.name}', description='{marketplace.description}'
                WHERE id={marketplace.id};
                """
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"""
                DELETE FROM marketplace
                WHERE id={id};
                """
        super().execute(query)

    def read_by_id(self, id: int) -> Marketplace:
        query = f"SELECT name, description, id FROM marketplace where id ={id};"
        marketplace = super().read(query)[0]
        results = Marketplace(marketplace[0], marketplace[1], marketplace[2])
        return results

