from datetime import date, datetime, timedelta
from Field import Field

class Birthday(Field):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    def __repr__(self) -> str:
        return f'{self.birthday:%d-%m-%Y}'

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, new_date):
        try:
            check_date = datetime.strptime(new_date, '%d-%m-%Y')
        except ValueError:
            print(f'Date is not correct. Ente date in format: (day)-(month)-(Year)')
            return self
        if check.date < datetime.now():
            self.__birthday = check_date.date()
        else:
            print('Birthday can not be in future')
