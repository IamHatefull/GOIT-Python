import pickle
from pathlib import Path

from Name import Name
from Phone import Phone
from Birthday import Birthday
from Record import Record
from AddressBook import AddressBook

end_cycle = False
address_book = AddressBook()


hello_func = lambda string: 'How can i help you?'

def serialize_pickle(address_book_path, address_book):
    with open(address_book_path, 'wb') as fh:
        pickle.dump(address_book, fh)

def deserialize_pickle(address_book_path):
    with open(address_book_path, 'rb') as fh:
        unpacked = pickle.load(fh)
    return unpacked   

#i don't use ValueError, because i want to allow use numbers as names for contact
def input_error(func):
    def inner(string):
        try:
            return func(string)
        except KeyError:
            return 'Wrong name, try again!'
        except IndexError:
            return 'Give me name and number, please!'
    return inner

@input_error            
def add_contact(string):
    string = string.split(' ')
    name = string[1]
    number = string[2]
    if name == '' or number == '':
        return 'Give me name and number, please!'
    obj_name = Name(name)
    obj_phone = Phone(number)
    obj_record = Record(obj_name)
    obj_record.add_phone(obj_phone)
    address_book.add_record(obj_record)
    return f'Contact with name {name} and number {number} was added'

@input_error
def get_phone(string):
    name = string.split(' ')[1]
    needed_record = address_book[name]
    return needed_record.phone_list

@input_error
def change_contact(string):
    string = string.split(' ')
    name = string[1]
    number = string[2]
    if name == '' or number == '':
        return 'Give me name and number, please!'
    obj_name = Name(name)
    obj_phone = Phone(number)
    needed_record =  address_book[obj_name.name]
    needed_record.add_phone(obj_phone)
    
    return f'Contact with name {name} changed number to {number}'

@input_error
def find(string):
    global address_book
    res = AddressBook()
    for key, value in address_book.items():
        if value.search(string):
            res[key] = value
    if not res:
        return 'wrong command! Try again, please!'
    return res
    

def show_contacts(string):
    global address_book
    for block in address_book.out_iterator():
            print(block)
            print('---------------------------------------------------------------------------------------------------')
            input('Press "Enter" to continue')
    return 'Output complete!...'

def finish_func(string):
    global end_cycle
    end_cycle = True
    return 'Goodbye!'
    
    
OPERATIONS = {
    'hello': hello_func,
    'add': add_contact,
    'change': change_contact,
    'phone': get_phone,
    'show': show_contacts,
    'goodbye': finish_func,
    'close': finish_func,
    'exit': finish_func
}

@input_error
def get_handler(operator):
    if not OPERATIONS.get(operator):
        return find
    return OPERATIONS[operator]

def main():
    
    #if file exist deseralize data
    path = Path('Address_Book.txt')
    global address_book
    if path.is_file():
        address_book = deserialize_pickle(path)
    


    while True:
        command = input('Input your command: ')
        operator = command.split(' ')[0].lower()
        if operator == '.':
            break
        handler = get_handler(operator)
        answer = handler(command)
        print(answer) 
        if end_cycle:
            serialize_pickle(path, address_book)
            break
        
if __name__ == '__main__':
    main()
