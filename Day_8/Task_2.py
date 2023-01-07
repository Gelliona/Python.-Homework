"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка (Cell). В его конструкторе инициализировать
параметр (quantity), соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление
клеток соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки
определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.

** - По желанию: В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет
организовать ячейки по рядам. Метод должен возвращать строку вида
***\n***\n***..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются
все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

Пример клиентского кода:
print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))

Результаты:
Создаем объекты клеток

Складываем
Сумма клеток = (55)

Вычитаем
Разность отрицательна, поэтому операция не выполняется
Разность клеток = (5)

Умножаем
Умножение клеток = (750)

Делим
Деление клеток = (1)

Организация ячеек по рядам
*****\n*****\n*****\n******\n******\n******
**********\n**********\n*****
"""


class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'Новая клетка {Cell(self.quantity + other.quantity)}'

    def __str__(self):
        return f"Cell({self.quantity})"

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return f'Новая клетка {Cell(self.quantity - other.quantity)}'
        else:
            return 'Разность отрицательна, значит вычитание не выполняется!'

    def __mul__(self, other):
        return f'Новая клетка {Cell(self.quantity * other.quantity)}'

    def __truediv__(self, other):
        return f'Новая клетка {Cell(self.quantity // other.quantity)}'

    def make_order(self, amount):     # amount - количество ячеек в одном ряду
        rows = self.quantity // amount
        remainder = self.quantity
        my_list = ['' for i in range(rows)]
        for i in range(rows):
            if remainder >= amount:
                my_list[i] = amount * '*'
            remainder -= amount
        if 0 < remainder < amount:
            my_list.append(remainder * '*')
        print('\\n'.join(my_list))


print("Создаем объекты клеток:")
cell1 = Cell(30)
cell2 = Cell(25)
print(cell1)
print(cell2)

print()

print("Складываем:")
print(cell1 + cell2)
print()
print("Вычитаем:")
print(cell1 - cell2)
print()
print("Умножаем:")
print(cell1 * cell2)
print()
print("Делим:")
print(cell1 / cell2)

print()
print("Организуем ячейки по рядам:")
cell1.make_order(5)
print()
cell2.make_order(10)
