"""
Функция генерирует список, выбирает из него элементы, значения
которых больше предыдущего элемента и вычисляет сумму этих элементов.
"""
import random
from memory_profiler import profile


@profile()
def my_func():
    my_list = [random.randint(1, 300) for el in range(100000)]
    result_list = [my_list[i] for i in range(1, 100000) if my_list[i]
                   > my_list[i-1]]
    my_list = None
    total = sum(result_list)
    result_list = None
    return total


print(my_func())

"""
При создании списков my_list и result_list в функции дополнительно
выделялась память. Чтобы освободить память, после завершения необходимых
манипуляций с этими списками, я принудительно переношу ссылки на эти списки
на более экономичный объект None. После этого используемая память возвращается
ближе к первоначально выделенному значению.
"""