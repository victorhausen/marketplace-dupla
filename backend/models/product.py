class Product:
    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        self.__name = name
        self.__description = description
        self.__price = price
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
