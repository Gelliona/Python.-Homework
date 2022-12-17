"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая
строка.
"""
my_string = input("Введите строку: ")
my_file = open('task1.txt', 'w', encoding='utf-8')
my_file.write(my_string + '\n')
my_file.close()
while my_string:
    my_string = input("Введите строку: ")
    i = 2
    if my_string == '':
        print("Запись завершена")
    else:
        my_file = open('task1.txt', 'a', encoding='utf-8')
        my_file.write(my_string + '\n')
        my_file.close()
