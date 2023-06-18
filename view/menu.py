from .in_out import input_return_int

class Menu:
    def __init__(self, choices: list):
        self.choices = choices

    def __str__(self) -> str:
        result = ''
        enum_menu = list(enumerate(self.choices, 1))
        for key, value in enum_menu:
            result += f'{key}. {value:<25}\n'
        return result

    def choice(self, message) -> int:
        upper = len(self.choices)
        return input_return_int(message, upper)


