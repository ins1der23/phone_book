from phone_book import PhoneBook
from contact import Contact
from contact_list import ContactList
from view import Menu, in_out, text
import services

def change_contact(pb: PhoneBook, contact_list: ContactList):
    uid = in_out.input_exact(text.input_index, contact_list.get_uids())
    to_change = pb.search_id(uid)
    old_name = to_change.name
    new_fields = in_out.input_fields(text.input_change_contact)
    if (services.check_fields(new_fields)):
        if (services.confirm_changes()):
            pb.replace(to_change, uid, new_fields)
            in_out.print_message(text.contact_changed(new_fields[0]))
        else: in_out.print_message(text.cancel_changes)
    else: in_out.print_message(text.contact_not_changed(old_name))

def delete_contact(pb: PhoneBook, contact_list: ContactList):
    uid = in_out.input_exact(text.input_index, contact_list.get_uids())
    name =  pb.search_id(uid).name
    if (services.confirm_changes()):
        pb.delete(uid)
        in_out.print_message(text.contact_deleted(name))
    else: (in_out.print_message(text.cancel_changes))