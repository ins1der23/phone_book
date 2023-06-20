from msvcrt import getch

from .text import *

def show_menu(menu: object):
    print(menu)
    
def show_contact_list(contact_list: object):
    print('\n' + '=' * 67)
    print(contact_list)
    print('=' * 67)


def show_contacts(book: list):
    if len(book) != 0:
        print('\n' + '=' * 67)
        for contact in book:
            print(contact)
        print('=' * 67)
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
        print(message)
        choice = getch()
        match choice:
            case b'\r': return True
            case b'\x1b': return False
            
            
def input_return(message: str) -> str:
    return input(message)
    
def input_return_int(message: str, upper: int) -> int:
    while True:
        uid = input(message)
        if uid.isdigit and 0 < int(uid) <= upper:
            return int(uid)
        else: print(input_error(upper))

def input_exact(message, uids: list[int]):
    while True:
        uid = input(message)
        if uid.isdigit and int(uid) in uids:
            return int(uid)
        else: print(exact_input_error(uids))