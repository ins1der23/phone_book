from phone_book import PhoneBook
from contact import Contact
from view import InOut
import services
from view import text


def start():
    pb = PhoneBook('phones.txt')
    pb.open_file()
    InOut.print_message(text.open_successful)
    while True:
        choice = InOut.menu()
        match choice:
            case 1:
                InOut.show_contacts(pb.contacts)
            case 2:
                new = InOut.input_fields(text.input_new_contact)
                if (services.check_fields(new) == False):
                    InOut.print_message(text.empty_fields)
                else:
                    if (services.confirm_changes()):
                        pb.add_contact(new)
                        InOut.print_message(text.contact_saved(new[0]))
                    else: InOut.print_message(text.cancel_changes)
            case 3:
                word = InOut.input_return(text.search_word).lower()
                result = pb.search(word)
                InOut.show_contacts(result)
            case 4:
                word = InOut.input_return(text.search_word)
                InOut.show_contacts(pb.search(word))
                upper = services.get_max_id()
                uid = InOut.input_return_int(text.input_index, upper)
                to_change = pb.search_id(uid)
                old_name = to_change.name
                new_fields = InOut.input_fields(text.input_change_contact)
                if (services.check_fields(new_fields)):
                    if (services.confirm_changes()):
                        pb.replace(to_change, uid, new_fields)
                        InOut.print_message(text.contact_changed(new_fields[0]))
                    else: InOut.print_message(text.cancel_changes)
                else: InOut.print_message(text.contact_not_changed(old_name))
            case 5:
                word = InOut.input_return(text.delete_word)
                InOut.show_contacts(pb.search(word))
                upper = services.get_max_id()
                uid = InOut.input_return_int(text.delete_index, upper)
                name =  pb.search_id(uid).name
                if (services.confirm_changes()):
                    pb.delete(uid)
                    InOut.print_message(text.contact_deleted(name))
                else: (InOut.print_message(text.cancel_changes))
            case 6:
                InOut.print_info(text.confirm_changes)
                if (InOut.input_yes(text.yes_choose)):
                    pb.save_file()
                    InOut.print_message(text.save_successful)
            case 7:
                if (services.confirm_changes()):
                    pb.save_file()
                    InOut.print_message(text.save_successful)
                else: (InOut.print_message(text.cancel_changes))
                break
                
