from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def get_name(self):
        self.name = name
        return Name(self.name)

class Phone(Field):
# реалізація класу Phone:
    def __init__(self, value):
        super().__init__(value)
# Реалізовано валідацію номера телефону (перевірка на 10 цифр).
        
    def get_phone(self): 
        if len(self.value) == 10 and self.value.isdigit():
            return  self.value
        else:
            print('Inwalid phone number')

class Record():
    # реалізація класу
    def __init__(self, name):
        self.name = Name(name)  # Реалізовано зберігання об'єкта Name в окремому атрибуті.
        self.phones = []  # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
      
# додавання 
    def add_phone(self, phone):
        phone_obj = Phone(phone) #
        phone_valid = phone_obj.get_phone() #
        if phone_valid: #
            self.phones.append(phone_valid)
            
# видалення
    def remove_phone(self, phone): 
        phone_obj = Phone(phone).get_phone()
        self.phones.remove(phone_obj)

# редагування 
    def edit_phone(self, phone, new_phone): 
        new_phone_obj = Phone(new_phone).get_phone()
        if phone in self.phones: #
            self.phones.remove(phone) 
            self.phones.append(new_phone_obj)
            print("Changes made")
            return self.phones
        else:
            print(" Phone is not in list")
            return None
                
# пошук об'єктів Phone
    def find_phone(self, phone):
        phone_obj = Phone(phone).get_phone()
        if phone_obj in self.phones:
            return self.phones
        else:
            print ("Don't find this number")

    def __str__(self):
        return f"\nIt's automatically printed.\nContact name: {self.name}, phones: {self.phones}\n"

class AddressBook(UserDict):
    def __init__(self):
        self.data={} # словник- книга контактів

 # Реалізовано метод add_record, який додає запис до self.data.  
    def add_record(self, contact):
        self.data[str(contact.name)] = contact.phones
        print(f"Contact added. \nName: {contact.name}, phones: {contact.phones}")
        return self.data
    
# Реалізовано метод find, який знаходить запис за ім'ям.
    def find(self, name):
        self.name = name
        for key, value in self.data.items():
            if self.name in str(key):
                print(f"Contact found. \nName: {name}, phones: {value}")
                p = Record(name) #реалізація Record-обєкту
                p.name = name 
                p.phones = value
                return p       # повернення Record() обєкту
            else:
                print (f"Don't find this name: {name}")
                return None
    
# Реалізовано метод delete, який видаляє запис за ім'ям.
    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
            print(f"Record for '{name}' deleted successfully.")
        else:
            print(f"Record for '{name}' not found in the address book.")
        
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("0004567890")
# Додавання запису John до адресної книги
book.add_record(john_record)
# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(name," ----",record)
# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: ['0004567890', '1112223333']
# Пошук конкретного телефону у записі John
found_phone = john.find_phone("1112223333")
print(f"{john.name}: {found_phone}")  # Виведення: John: ['0004567890', '1112223333']
# Видалення запису Jane
book.delete("Jane")
print(book)