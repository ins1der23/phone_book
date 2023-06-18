from contact import Contact

class ContactList:

    def __init__(self, contacts: list[Contact]):
        self.contacts = contacts

    def __str__(self) -> str:
        result = ''
        for contact in self.contacts:
            result += f'{contact.uid:<3} {contact.name:<20} {contact.phone:<20} {contact.comment:<20}\n'
        return result.strip()

    def get_uids(self) -> list[int]:
        result = []
        for contact in self.contacts:
            result.append(contact.uid)
        return result
    