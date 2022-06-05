'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_division():
    try:
        divider = int(input("Enter the divider >>> "))
        denominator = int(input("Enter the denominator >>> "))
        if denominator == 0:
            raise DivisionByZero("Division by zero exception!")
        else:
            total = divider / denominator
            return f"Division result >>> {divider} / {denominator} = {total}"
    except ValueError:
        return "Incorrect input. Please, enter number"
    except DivisionByZero as my_error:
        return my_error


print(my_division())
