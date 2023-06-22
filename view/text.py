main_menu = ['Показать все контакты',
             'Создать новый контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Сохранить изменения',
             'Выход']
contact_menu = ['Изменить контакт',
                'Удалить контакт',
                'Возврат в главное меню']

menu_choice = 'Выберите пункт меню: '

book_error = 'Телефонная книга пуста или файл не открыт'

open_successful = 'Телефонная книга успешно открыта'
save_successful = 'Телефонная книга успешно сохранена'

input_new_contact = 'Введите данные нового контакта: '
new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите коммент: ']
empty_fields = 'Контакт не может быть пустым'
search_word = 'Введите искомый элемент: '
input_index = 'Введите индекс изменяемого контакта или 0 для отмены: '
input_change_contact = 'Введите данные изменяемого контакта или Enter, чтобы оставить без изменений: '
change_word = 'Введите контакт для изменения:  '
delete_word = 'Введите удаляемый контакт: '
delete_index = 'Введите индекс удаляемого контакта: '
phones_chaged = 'Телефонная книга была изменена'
yes_choose = 'Нажмите Enter для подтверждения или Esc для отмены '
confirm_changes = 'Применить изменения?'
cancel_changes = 'Изменения не были применены'

def contact_saved(name: str):
    return f'Контакт {name} успешно сохранен'

def changing_intension(name: str):
    return f'Вы собираетесь изменить контакт {name}'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменен'

def contact_not_changed(name: str):
    return f'Контакт {name} не изменен'

def deleting_intension(name:str):
    return f'Вы собираетесь удалить контакт {name}'

def contact_deleted(name: str):
    return f'Контакт {name} удален'

def input_int(upper: int):
    return f'Введите число от 1 до {upper}: '

def input_error(upper: int):
    return f'Некорректный ввод. Введите число от 1 до {upper}: ' 

def exact_input_error(numbers: list[int]):
    return f'Некорректный ввод. Введите число из списка: {str(numbers).strip("[]")} ' 


