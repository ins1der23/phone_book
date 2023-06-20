class Contact:
    count_id = 1

    def __init__(self, name: str, phone: str, comment: str):
        
        self.uid = Contact.count_id
        self.name = name
        self.phone = phone
        self.comment = comment
        Contact.count_id +=1

    def __str__(self) -> str:
        return f'{self.uid:<3} {self.name:<20} {self.phone:<20} {self.comment:<20}'
    
    def for_search(self):
        return f'{self.uid} {self.name} {self.phone} {self.comment}'.lower()
    
    def change(self, uid, fields: tuple):
        self.uid = uid
        self.name = fields[0] if fields[0] != '' else self.name
        self.phone = fields[1] if fields[1] != '' else self.phone
        self.comment = fields[2] if fields[2] != '' else self.comment

  


