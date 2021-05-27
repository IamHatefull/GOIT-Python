from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record.phone_list

class Field():
    pass

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Record(Field):

    def __init__(self, name):
        self.name = name
        self.phone_list = []
+
    def add_phone(self, phone):
        self.phone_list.append(phone)

    def delete_phone(self, phone):
        self.phone_list.remove(phone)

    def change_phone(self, old_phone, new_phone):
        ind = self.phone_list.index(old_phone)
        self.phone_list.remove(phone)
        self.phone_list.insert(ind, new_phone)




