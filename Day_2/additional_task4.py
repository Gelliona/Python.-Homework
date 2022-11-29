"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся
в файле file.txt в одной строке одно число.
"""
num = int(input("Введите целое число: "))
i = -num
my_list = []
while i <= num:
    my_list.append(i)
    i +=1
print(my_list)

product = 1
data = open('file.txt', 'r')
for line in data:
    if int(line) < len(my_list):
        product *= my_list[int(line)]
    else:
        break
data.close()
print(product)
