"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

def to_divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Деление на 0!"

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(to_divide(a, b))
except ValueError:
    print("Вводите числа!")

