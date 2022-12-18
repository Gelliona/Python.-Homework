"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
"""
from timeit import timeit

decimal_num = int(input("Введите целое число: "))

'Моё решение'

binary_list = []


def to_binary(num):
    if num < 2:
        binary_list.append(1)
        return binary_list
    else:
        binary_list.append(num % 2)
        return to_binary(num // 2)


'Альтернативное решение'


def to_binary_new(num):
    binary_list2 = []
    while num > 0:
        binary_list2.insert(0, num % 2)
        num = num // 2
    return binary_list2


binary_num = to_binary(decimal_num)
binary_num.reverse()
for el in binary_num:
    print(el, end="")

print()
binary_num2 = to_binary_new(decimal_num)
for el in binary_num2:
    print(el, end="")

print()
print()
print("Затраты времени при расчете моим способом: ")
print(timeit("to_binary(decimal_num)", globals=globals(), number=10000))
print()
print("Затраты времени при расчете альтернативным способом: ")
print(timeit("to_binary_new(decimal_num)", globals=globals(), number=10000))


"""
Данная задача была мной выполнена с помощью функции to_binary.
Чтобы рассмотреть вариант оптимизации задачи, добавила альтернативный вариант
решения с использованием цикла while.
Как показали замеры времени, в данном случае альтернативный вариант
предпочтительнее, так как менее затратен по времени. 
Цикл while работает быстрее рекурсии, потому что в цикле просходит простой 
итеративный процесс, а каждый новый вызов функции в рекурсии занимает
больше времени и ресурсов.
"""