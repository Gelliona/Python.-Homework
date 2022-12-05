"""
Напишите программу, которая принимает на вход вещественное число и показывает
сумму его цифр.
"""
num = (input("Введите число: ")).split('.')
first_part = int(num[0])
if len(num) == 2:
    second_part = int(num[1])
else:
    second_part = 0
summa = 0
while first_part != 0:
    summa += first_part % 10
    first_part = first_part // 10
while second_part != 0:
    summa += second_part % 10
    second_part = second_part // 10
print(f'Сумма цифр в этом числе равна {summa}')
