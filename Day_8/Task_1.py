"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков)
для формирования матрицы. [[], [], []]

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""
from random import randint


class Matrix:

    def __init__(self, data):
        self.new_list = data

    def __str__(self):
        s = '\n'.join(('\t'.join(str(i) for i in row)
                       for row in self.new_list))
        return s

    def __add__(self, other):
        for i in range(3):
            for j in range(3):
                self.new_list[i][j] += other.new_list[i][j]
        return Matrix(self.new_list)


matrix1 = Matrix([[randint(0, 10) for a in range(3)],
                  [randint(0, 10) for b in range(3)],
                  [randint(0, 10) for c in range(3)]])
matrix2 = Matrix([[randint(0, 10) for d in range(3)],
                  [randint(0, 10) for e in range(3)],
                  [randint(0, 10) for f in range(3)]])
print("Матрица 1:")
print(matrix1)
print("Матрица 2:")
print(matrix2)
print("Сумма матриц")
print(matrix1 + matrix2)
