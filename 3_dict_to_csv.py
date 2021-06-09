"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

staffs = [
    {'name': 'Иван', 'age': '25', 'job':'Директор'},
    {'name': 'Петр', 'age': '40', 'job':'Заместитель'},
    {'name': 'Сергей', 'age': '38', 'job':'Бухгалтер'},
    {'name': 'Степан', 'age': '18', 'job':'Все остальное'}
]


def main():
    try:
        with open('staff.csv', 'w', encoding='utf-8') as f:
            fields = ['name', 'age', 'job']
            writer = csv.DictWriter(f, fields, delimiter='\t')
            writer.writeheader()
            for staff in staffs:
                writer.writerow(staff)
            print('Файл создан')
    except ValueError:
        print('ValueError')


if __name__ == "__main__":
    main()
