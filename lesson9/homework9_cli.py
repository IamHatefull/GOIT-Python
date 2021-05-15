end_cycle = False
contact_dict = {}

hello_func = lambda string: 'How can i help you?'
key_except_func = lambda string: 'wrong command! Try again, please!'

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
    contact_dict[name] = number
    return f'Contact with name {name} and number {number} was added'

@input_error
def get_phone(string):
    name = string.split(' ')[1]
    return contact_dict[name]

@input_error
def change_contact(string):
    string = string.split(' ')
    name = string[1]
    number = string[2]
    if name == '' or number == '':
        return 'Give me name and number, please!'
    contact_dict[name] = number
    return f'Contact with name {name} changed number to {number}'

def show_contacts(string):
    contact_list = []
    for name, number in contact_dict.items():
        contact_list.append(f'{name}: {number}')
    return '\n'.join(contact_list)

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
        return key_except_func
    return OPERATIONS[operator]

def main():
    while True:
        command = input('Input your command: ')
        operator = command.split(' ')[0].lower()
        if operator == '.':
            break
        handler = get_handler(operator)
        answer = handler(command)
        print(answer) 
        if end_cycle:
            break
        
main()
