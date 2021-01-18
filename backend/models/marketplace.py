class Marketplace:
    def __init__(self, name: str, description: str, id: int = None):
        self.__name = name
        self.__description = description
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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
