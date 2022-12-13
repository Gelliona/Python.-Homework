"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться
на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
my_file = open('task4_reading.txt', 'r', encoding='utf-8')
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

for line in my_file:
    line = line.strip()
    print(line)
    for key in my_dict:
        if line.startswith(key):
            new_line = line.replace(key, my_dict[key])
            new_file = open('task4_writing.txt', 'a', encoding='utf-8')
            new_file.write(new_line + '\n')

my_file.close()
