main_menu = ['Показать все контакты',
             'Создать новый контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Сохранить изменения',
             'Выход']

menu_choice = 'Выберите пункт меню: '

book_error = 'Телефонная книга пуста или файл не открыт'

open_successful = 'Телефонная книга успешно открыта'
save_successful = 'Телефонная книга успешно сохранена'

input_new_contact = 'Введите данные нового контакта'
new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите коммент: ']
empty_fields = 'Контакт не может быть пустым'
search_word = 'Введите искомый элемент: '
input_index = 'Введите индекс изменяемого контакта: '
input_change_contact = 'Введите данные изменяемого контакта или Enter, чтобы оставить без изменений: '
delete_word = 'Введите удаляемый элемент: '
delete_index = 'Введите индекс удаляемого контакта: '
phones_chaged = 'Телефонная книга была изменена'
save_changes = 'Хотите сохранить изменения? '
yes_choose = 'Введите Y для потдверждения или N для отмены '
confirm_changes = 'Сохранить изменения?'
cancel_changes = 'Изменения не были применены'

def contact_saved(name: str):
    return f'Контакт {name} успешно сохранен'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменен'

def contact_not_changed(name: str):
    return f'Контакт {name} не изменен'

def contact_deleted(name: str):
    return f'Контакт {name} удален'

def input_int(upper: int):
    return f'Введите число от 1 до {upper}: '

def input_error(upper: int):
    return f'Некорректный ввод. Введите число от 1 до {upper}: ' 

