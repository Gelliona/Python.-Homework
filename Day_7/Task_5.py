"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Отрисовка ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Отрисовка карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Отрисовка маркером'


stat1 = Pen('Pen')
stat2 = Pencil('Pencil')
stat3 = Handle('Handle')

print(stat1.draw())
print(stat2.draw())
print(stat3.draw())
