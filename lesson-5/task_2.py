"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open('task_2_read.txt', 'r', encoding='UTF=8') as file:
    number_line = 0
    for lines in file.readlines():
        number_line += 1
        words = len([a for a in lines.split(' ') if a != '' and a != '\n'])
        print(f'В {number_line} строке {words} слов')
    print("Колличество строк:", number_line)
