from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self[record.name.name] = record

    def __repr__(self) -> str:
        res = ''
        for key, value in self.items():
            res +=f'|| {key} || : {value.__repr__()}'
        return res
    
    def out_iterator(self,N = 10):
        k = 0
        key_list = list(self)
        key_list_max = len(key_list)
        while k < key_list_max:
            result = AddressBook()
            max_iter = key_list_max if len(key_list[k:]) < N else k + N
            for i in range(k, max_iter):
                result.add_record(self[key_list[i]])
                k += 1
            yield result
