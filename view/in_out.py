from .text import *
from contact import Contact

class InOut:

    def menu() -> int:
        print(main_menu)
        while True:
            choice = input(menu_choice)
            if choice.isdigit() and 0 < int(choice) < 9:
                return int(choice)
        print(input_error)


    def show_contacts(book: list):
        if len(book) != 0:
            print('\n' + '=' * 67)
            for contact in book:
              print(contact)
            print('=' * 67 + '\n')
        else:
            print(book_error)

    def input_fields(message: str) -> tuple:
        print(message)
        return (input(new_contact[0]),input(new_contact[1]),input(new_contact[2]))
         
         
    def print_message(message: str):
        length = len(message)
        print('\n' + '=' * length)
        print(message)
        print('=' * length + '\n')

    def print_info(message: str):
        length = len(message)
        print('\n' + '-' * length)
        print(message)
        print('-' * length + '\n')

    def input_yes (message: str) -> bool:
        while True:
            choice = input(message)
            if choice.upper() == 'Y':
                return True
            elif choice.upper() == 'N':
                return False
            
    def input_return(message: str) -> str:
        return input(message)
    
    def input_return_int(message: str, upper: int) -> int:
        while True:
            uid = input(message)
            if uid.isdigit and 0 < int(uid) < upper:
                return int(uid)