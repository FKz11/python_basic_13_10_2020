"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def sum_line(my_line):
    my_sum = 0
    number = ''
    for i in my_line:
        if i.isdigit():
            number += i
            flag = True
        else:
            flag = False
        if not flag and number:
            my_sum += int(number)
            number = ''
    return my_sum


with open('task_6_read.txt', 'r', encoding='UTF=8') as file:
    dictionary = dict()
    for lines in file.readlines():
        dictionary[lines.split(' ')[0][:-1]] = sum_line(lines)
    print(dictionary)
