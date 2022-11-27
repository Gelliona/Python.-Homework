"""
Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который результат
спортсмена составит не менее b километров. Программа должна принимать значения
параметров a и b и выводить одно натуральное число — номер дня.
"""
a = int(input("Введите результат в первый день: "))
b = int(input("Введите желаемый результат: "))
day_result = a
day = 1
while day_result < b:
    day += 1
    day_result = day_result / 100 * 10 + day_result
print(f'На {day}-й день спортсмен достиг результата - не менее {b} км')