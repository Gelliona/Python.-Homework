"""
Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции.
"""
num = int(input("Введите целое положительное число: "))
max_digit = 0
while num != 0:
    last_digit = num % 10
    num = num // 10
    if last_digit > max_digit:
        max_digit = last_digit
print(max_digit)