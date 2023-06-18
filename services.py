from contact import Contact
from view import in_out
from view import text

def confirm_changes() -> bool:
    in_out.print_info(text.confirm_changes)
    if (in_out.input_yes(text.yes_choose)): return True
    else: return False

def check_fields(fields: tuple) -> bool:
    flag = True
    for item in  fields:
        if (item != ''): 
            flag = True
            break
        else: flag = False
    return flag

def get_max_id()-> int:
    return Contact.count_id - 1