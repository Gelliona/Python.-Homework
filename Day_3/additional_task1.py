"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
элементов списка, стоящих на нечётной позиции.
"""

my_list = [3, 5, 7, 9, 2, 5, 8, 4]
print(my_list)
total = 0
for i in range(1, len(my_list), 2):
    total += my_list[i]
print(f'Сумма чисел на нечетных позициях равна {total}')
