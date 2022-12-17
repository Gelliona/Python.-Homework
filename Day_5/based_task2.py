"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_file = open('task2.txt', 'r', encoding='utf-8')
strings = 0
words = 0
for line in my_file:
    line = line.strip()
    strings += 1
    words += len(line.split())
    print(f'Строка "{line}" содержит {words}'
          f'{" слов" if words > 4 else " слова"}')
    words = 0
print(f'Всего в файле {strings} строк')

my_file.close()
