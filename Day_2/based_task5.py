"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
my_list = [7, 5, 3, 3, 2]
new_num = int(input("Введите новый элемент рейтинга: "))
for i in range(len(my_list)-1, -1, -1):
    if my_list[i] == new_num:
        my_list.insert(i, new_num)
        break
print(my_list)

