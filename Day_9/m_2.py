"""
Функции принимают число от 1 до 12 и сообщают, к какому времени года относится
месяц под этим номером (зима, весна, лето, осень). Функции работают
со словарем и списком.
"""


def find_season_dict(month):
    year_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
                 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
                 11: 'осень', 12: 'зима'}
    return f'{month}-й месяц - это {year_dict[month]}'


def find_season_list(month):
    year_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето',
                 'лето', 'осень', 'осень', 'осень', 'зима']
    return f'{month}-й месяц - это {year_list[month - 1]}'



