"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""
import random

my_file = open('task5.txt', 'w', encoding='utf-8')
for i in range(20):
    number = random.randint(1, 100)
    my_file.write(f'{number} ')
my_file.close()

my_file = open('task5.txt', 'r', encoding='utf-8')
content = my_file.read().split()
total = 0
for el in content:
    total += int(el)


my_file.close()
print(f'Сумма всех чисел в файле - {total}')
