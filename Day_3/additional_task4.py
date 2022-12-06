"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
"""
decimal_num = int(input("Введите целое число: "))


def to_binary(num, binary_list=[]):
    if num < 2:
        binary_list.append(1)
        return binary_list
    else:
        binary_list.append(num % 2)
        return to_binary(num // 2, binary_list)


binary_num = to_binary(decimal_num)
binary_num.reverse()
for el in binary_num:
    print(el, end="")
