"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.
"""
my_file = open('task3.txt', 'r', encoding='utf-8')

my_list = []
employees = []
count = 0
total = 0

for line in my_file:
    print(line)
    my_list = line.split()
    total += float(my_list[1])
    count += 1
    if float(my_list[1]) > 20000:
        employees.append(my_list[0])

print()
print(f'Сотрудники с зарплатой более 20000: {", ".join(employees)}')
print(f'Средняя зарплата сотрудников {round(total/count, 2)}')

my_file.close()
