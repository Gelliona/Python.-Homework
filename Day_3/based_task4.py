"""
Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора возведения в степень.
Второй — более сложная реализация без оператора возведения в степень,
предусматривающая использование цикла.
"""


def my_func1(x, y):
    return round(x**y, 4)


def my_func2(x, y):
    total = 1
    for i in range(abs(y)):
        total *= 1 / x
    return round(total, 4)


a = float(input("Введите любое положительное число: "))
b = int(input("Введите целое отрицательное число: "))
print(f'{a} в степени {b} при расчете первым способом равно {my_func1(a, b)}')
print(f'{a} в степени {b} при расчете вторым способом равно {my_func2(a, b)}')
