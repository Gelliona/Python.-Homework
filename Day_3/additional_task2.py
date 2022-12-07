"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
"""

my_list = [int(i) for i in input("Введите несколько целых чисел через пробел ")
           .split()]
print(my_list)
new_list = []
for i in range((len(my_list)+1)//2):
    new_list.append(my_list[i] * my_list[-1-i])
print(new_list)



