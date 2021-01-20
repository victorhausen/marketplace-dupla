from backend.models.marketplace import Marketplace
from backend.dao_db.base_dao import BaseDao


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)