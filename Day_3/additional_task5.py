"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для
отрицательных индексов.
"""
num = int(input("Введите целое число: "))

first = 0
second = 1
my_list = [second, first, second]
i = 2
while i <= num:
    my_list.append(first + second)
    if i % 2 == 0:
        my_list.insert(0, -(first + second))
    else:
        my_list.insert(0, first + second)
    first, second = second, first + second
    i += 1

print(my_list)
