from backend.dao_db.marketplace_dao_db import MarketplaceDao
from backend.controller.base_controller import BaseController


class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao, "Marketplace")

# creating_log(Log(current_date(), 'create', 'marketplace'))
