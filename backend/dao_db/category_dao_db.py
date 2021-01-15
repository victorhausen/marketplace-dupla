from backend.models.category import Category
from backend.dao_db.base_dao import BaseDao


class CategoryDao(BaseDao):
    def create(self, category: Category) -> None:
        query = f"""
                INSERT INTO category 
                (name, description) 
                values
                ('{category.name}', '{category.description}');
                """
        super().execute(query)

    def read_all(self) -> list:
        categories = []
        query = "SELECT name, description, id FROM category;"
        list_categories = super().read(query)
        for category in list_categories:
            result = Category(category[0], category[1], category[2])
            categories.append(result)
        return categories

    def update(self, category: Category) -> None:
        query = f"""
                UPDATE category
                SET name='{category.name}', description='{category.description}'
                WHERE id={category.id};
                """
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"""
                DELETE FROM category
                WHERE id={id};
                """
        super().execute(query)

    def read_by_id(self, id: int) -> Category:
        query = f"SELECT name, description, id  FROM category WHERE id={id};"
        categories = super().read(query)[0]
        results = Category(categories[0], categories[1], categories[2])
        return results