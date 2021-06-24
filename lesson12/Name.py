from Field import Field

class Name(Field):
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
