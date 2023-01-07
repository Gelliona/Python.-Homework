"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZero(Exception):
    def __init__(self, text):
        self.text = text


def divide_by_zero(devidend, diviser):
    try:
        if diviser == 0:
            raise DivisionByZero("Делить на ноль нельзя!")
        print(devidend/diviser)
    except DivisionByZero as err:
        print(err.text)


inp_a = int(input("Введите положительное число: "))
inp_b = int(input("Введите положительное число: "))

divide_by_zero(inp_a, inp_b)
