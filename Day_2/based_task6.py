"""
*Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные
у пользователя.
"""


def filling_product_card():
    product_code = int(input("Введите артикул товара: "))
    product_name = (input("Введите наименование товара: "))
    product_price = float(input("Введите цену товара: "))
    product_quantity = int(input("Введите количество товара: "))
    product_unit = (input("Введите единицу измерения количества товара: "))
    product_dict = {'название': product_name, 'цена': product_price,
                    'количество': product_quantity, 'ед.': product_unit}
    product_tuple = (product_code, product_dict)
    return product_tuple


product_list = []
answer = input("Ввести новый товар? (Y/N)")
while answer.upper() != 'N':
    new_product = filling_product_card()
    product_list.append(new_product)
    answer = input("Ввести новый товар? (Y/N)")

print(product_list)
print()

print("Аналитика:")
goods_dict = {}
for j in range(0, 4):
    name_list = []
    new_key = []
    for i in range(len(product_list)):
        my_tuple = product_list[i]
        my_dict = my_tuple[1]
        name_list.append(my_dict[list(my_dict.keys())[j]])
        new_key.append(list(my_dict.keys())[j])
    goods_dict[list(set(new_key))[0]] = name_list

print(goods_dict)
