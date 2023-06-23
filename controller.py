from phone_book import PhoneBook
from contact import Contact
from contact_list import ContactList
from view import Menu, in_out, text
import services
import contr_methods

def start():
    pb = PhoneBook('phones.txt')
    pb.open_file()
    in_out.print_message(text.open_successful)
    while True:
        main_menu = Menu(text.main_menu)
        in_out.show_menu(main_menu)
        choice = main_menu.choice(text.input_int(len(main_menu.choices)))
        match choice:
            case 1:
                in_out.show_contacts(pb.contacts)
            case 2:
                new = in_out.input_fields(text.input_new_contact)
                if (services.check_fields(new) == False):
                    in_out.print_message(text.empty_fields)
                else:
                    if (services.confirm_changes()):
                        pb.add_contact(new)
                        in_out.print_message(text.contact_saved(new[0]))
                    else: in_out.print_message(text.cancel_changes)
            case 3:
                word = in_out.input_return(text.search_word)
                result = ContactList(pb.search(word))
                in_out.show_contact_list(result)
                while True:
                    contact_menu = Menu(text.contact_menu)
                    in_out.show_menu(contact_menu)
                    choice = contact_menu.choice(text.input_int(len(contact_menu.choices)))
                    match choice:
                        case 1: 
                            contr_methods.changing_contact(pb, result)
                            break
                        case 2: 
                            contr_methods.deleting_contact(pb, result)
                            break 
                        case 3: break
            case 4:
                word = in_out.input_return(text.change_word)
                result = ContactList(pb.search(word))
                in_out.show_contact_list(result)
                contr_methods.changing_contact(pb, result)
            case 5:
                word = in_out.input_return(text.delete_word)
                result = ContactList(pb.search(word))
                in_out.show_contact_list(result)
                contr_methods.deleting_contact(pb, result)
            case 6:
                in_out.print_info(text.confirm_changes)
                if (in_out.input_yes(text.yes_choose)):
                    pb.save_file()
                    in_out.print_message(text.save_successful)
            case 7:
                pb.save_temp_file()
                if pb.compare_files():
                    in_out.print_info(text.phones_chaged)
                    if (services.confirm_changes()):
                        pb.save_file()
                        in_out.print_message(text.save_successful)
                    else:
                        in_out.print_message(text.cancel_changes)
                pb.delete_temp()
                break
                
                
