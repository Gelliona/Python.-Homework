"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


# income = {"wage": wage, "bonus": bonus}
worker_1 = Position("Иван", "Иванов", "Охранник", 30500, 1000)
worker_2 = Position("Петр", "Петров", "Директор", 120800, 8000)
worker_3 = Position("Семён", "Семёнов", "Водитель", 45300, 2500)

print(worker_1.get_full_name())
print(f'Должность: {worker_1. position}')
print(f'Полная заработная плата: {worker_1.get_total_income()}')
print()
print(worker_2.get_full_name())
print(f'Должность: {worker_2. position}')
print(f'Полная заработная плата: {worker_2.get_total_income()}')
print()
print(worker_3.get_full_name())
print(f'Должность: {worker_3. position}')
print(f'Полная заработная плата: {worker_3.get_total_income()}')
