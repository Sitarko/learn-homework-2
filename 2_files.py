"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    try:
        with open('referat.txt', 'r', encoding='utf-8') as f:
            text = f.read()
            print (f'Длинна строки: {str(len(text))} симовла(ов)')
            word_count = len(text.split())
            print (f'В тексте {word_count} слов(а)')
        with open('referat2.txt', 'w', encoding='utf-8') as f_new:
            text = text.replace('.', '!')
            f_new.write(text)
            print('Файл referat2.txt создан')
    except FileNotFoundError:
        print('Файл не найден!')

if __name__ == "__main__":
    main()
