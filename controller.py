from phone_book import PhoneBook
from contact import Contact
from view import Menu, in_out, text
import services

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
                word = in_out.input_return(text.search_word).lower()
                result = pb.search(word)
                in_out.show_contacts(result)
            case 4:
                word = in_out.input_return(text.search_word)
                in_out.show_contacts(pb.search(word))
                upper = services.get_max_id()
                uid = in_out.input_return_int(text.input_index, upper)
                to_change = pb.search_id(uid)
                old_name = to_change.name
                new_fields = in_out.input_fields(text.input_change_contact)
                if (services.check_fields(new_fields)):
                    if (services.confirm_changes()):
                        pb.replace(to_change, uid, new_fields)
                        in_out.print_message(text.contact_changed(new_fields[0]))
                    else: in_out.print_message(text.cancel_changes)
                else: in_out.print_message(text.contact_not_changed(old_name))
            case 5:
                word = in_out.input_return(text.delete_word)
                in_out.show_contacts(pb.search(word))
                upper = services.get_max_id()
                uid = in_out.input_return_int(text.delete_index, upper)
                name =  pb.search_id(uid).name
                if (services.confirm_changes()):
                    pb.delete(uid)
                    in_out.print_message(text.contact_deleted(name))
                else: (in_out.print_message(text.cancel_changes))
            case 6:
                in_out.print_info(text.confirm_changes)
                if (in_out.input_yes(text.yes_choose)):
                    pb.save_file()
                    in_out.print_message(text.save_successful)
            case 7:
                if (services.confirm_changes()):
                    pb.save_file()
                    in_out.print_message(text.save_successful)
                else: (in_out.print_message(text.cancel_changes))
                break
                
