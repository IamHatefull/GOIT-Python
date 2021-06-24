from Field import Field

class Phone(Field):
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    def __repr__(self):
        return self.phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        trans_phone = phone.translate(str.maketrans('     ', '+() -'))
        if trans_phone.isdigit():
            self.__phone = trans_phone
        else:
            raise ValueError('Typed phone number is not correct. Try again!')
