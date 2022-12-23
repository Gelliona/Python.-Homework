"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат. Выполните вызов методов и также покажите
результат.
"""


class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км/ч'

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} - не полицейская машина'


class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Скорость превышена!"
        else:
            return f'Текущая скорость {self.name} - {self.speed} км/ч'


class SportCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Скорость превышена!"
        else:
            return f'Текущая скорость {self.name} - {self.speed} км/ч'


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


car1 = TownCar('LADA', 'Red', 90, False)
car2 = PoliceCar('FORD', 'White', 120, True)
car3 = WorkCar('MAZDA', 'Yellow', 90, False)
car4 = SportCar('BMW', 'Blue', 200, False)

print(car1.go())
print(car1.turn('направо'))
print(car1.show_speed())
print(car2.go())
print(car2.police())
print(car2.show_speed())
print(car2.turn('налево'))
print(car2.stop())
print(f'Марка этого автомобиля - {car3.name}. Его цвет - {car3.color}')
print(car3.go())
print(car4.police())
print(car4.show_speed())

