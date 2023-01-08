"""
Функция принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""


def set_of_products(n):
    my_list = []
    product = 1
    for i in range(1, n + 1):
        product *= i
        my_list.append(product)
    return my_list
