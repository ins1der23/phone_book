from contact import Contact

class PhoneBook:

    def __init__(self, path:str):
        self.contacts: list[Contact] = []
        self.path = path
        self.temp_path = f'${self.path}'

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            _, name, phone, comment, *_ = contact.strip().split(':')
            self.contacts.append(Contact(name, phone, comment))

    def add_contact(self, fields: tuple):
        self.contacts.append(Contact(fields[0], fields[1], fields[2]))

    def search(self, word: str) -> list[Contact]:
        result = []
        for contact in self.contacts:
            if word.lower() in contact.for_search():
                result.append(contact)
        return result
    
    def search_id(self, uid: int) -> Contact:
        result = None
        for contact in self.contacts:
            if uid == contact.uid:
                result = contact
        return result
    
    def replace(self, to_change: Contact, uid: int, fields: tuple):
        to_change.change(uid, fields)

    def delete(self, index: int):
        del self.contacts[index-1]

    def save_temp_file(self):
        data=''
        for contact in self.contacts:
                data += f"{contact.uid}:{contact.name}:{contact.phone}:{contact.comment}\n"
        with open (self.temp_path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def compare_files(self) -> bool:
        with open(self.temp_path, 'r', encoding='UTF-8') as file:
            temp_data = file.readlines()
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        if data != temp_data: return True
        else: return False

    def save_file(self):
        data=''
        for contact in self.contacts:
                data += f"{contact.uid}:{contact.name}:{contact.phone}:{contact.comment}\n"
        with open (self.path, 'w', encoding='UTF-8') as file:
            file.write(data)