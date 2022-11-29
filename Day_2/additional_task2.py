"""
Напишите программу, которая принимает на вход число N и выдает набор
произведений чисел от 1 до N.
"""
num = int(input("Введите целое число: "))
my_list = []
product = 1
for i in range(1, num + 1):
    product *= i
    my_list.append(product)
print(my_list)
