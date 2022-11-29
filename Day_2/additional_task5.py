"""
Реализуйте алгоритм перемешивания списка.
"""
import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Исходный список - {my_list}')
random.shuffle(my_list)
print(f'Список после перемешивания - {my_list}')
