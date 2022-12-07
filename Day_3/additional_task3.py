"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.
"""
my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(my_list)
print()
new_list = my_list

for i in range(len(my_list)):
    new_list[i] = round(my_list[i] - int(my_list[i]), 2)

if 0 in new_list:
    new_list.remove(0)

print(f'Максимальное значение дробной части - {max(new_list)}')
print(f'Минимальное значение дробной части - {min(new_list)}')
print(f'Разница между максимальным и минимальным значениями - '
      f'{max(new_list) - min(new_list)}')
