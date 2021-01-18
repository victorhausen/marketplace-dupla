class Seller:
    def __init__(self, name: str, phone: str, email: str, id: int = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id