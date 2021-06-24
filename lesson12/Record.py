from datetime import date, datetime, timedelta
from Field import Field

class Record(Field):

    def __init__(self, name, birthday = None):
        self.name = name
        self.phone_list = []
        self.birthday = birthday

    def __repr__(self):
        st = f"| {self.name.name:}| {self.birthday:} | {self.phone_list} |\n"
        '''if len(self.phone) > 1:
            for elem in self.phone[1:]:
                st += f"|                     |             | {elem: <16} |\n"'''
        return st

    def add_phone(self, phone):
        self.phone_list.append(phone)

    def delete_phone(self, phone):
        self.phone_list.remove(phone)

    def change_phone(self, old_phone, new_phone):
        ind = self.phone_list.index(old_phone)
        self.phone_list.remove(phone)
        self.phone_list.insert(ind, new_phone)

    def search(self, string):
        if string.casefold() in self.name.name.casefold():
            return self
        for num in self.phone_list:
            if string.casefold() in num.phone.casefold():
                return self
        return False

    def days_to_birthday(self):
        if date.today() > self.birthday.replace(year=date.today().year):
            return (self.birthday.replace(year=date.today().year + 1) - date.today()).days
        return (self.birthday.replace(year=date.today().year) - date.today()).days
