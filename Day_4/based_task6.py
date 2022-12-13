"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import cycle, count

start_num = int(input('Введите первое число: '))
finish_num = start_num ** 2

for i in count(start_num):
    if i < finish_num:
        print(i)
    else:
        break


my_list = [i for i in range(finish_num)]
count = 0
for el in cycle(my_list):
    if count < finish_num * 2:
        print(el)
        count += 1
    else:
        break
