"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой.
"""


def user_info(**info):
    print('Данные пользователя: ')
    for k in info.values():
        print(k, end=' ')


user_info(user_name='Ivan', user_surname='Ivanov',
          user_birthyear=1985, user_city='Moscow',
          user_email='ivaiva@mail.ru', user_phone=89964736283)
