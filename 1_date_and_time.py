"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days(date_now):

    dt1 = timedelta(days = 1)
    yesterday = date_now - dt1

    dt2 = timedelta(days = 30)
    month = date_now - dt2
    
    print ('Вчера: ' + str(yesterday), '\nСегодня: ' + str(date_now), '\n30 дней назад: ' + str(month))


def str_2_datetime(date_string):
    date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date 

if __name__ == "__main__":
    print_days(datetime.now())
    print(str_2_datetime("01/01/20 12:10:03.234567"))
