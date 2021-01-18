class Seller:
    def __init__(self, name: str, phone: str, email: str, id: int = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str) -> None:
        self.__phone = phone

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id