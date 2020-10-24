"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""


# Решение пункта а


def enter(line):
    number = input(line)
    try:
        assert float(number) % 1 == 0
        return number
    except ValueError:
        return enter(line)
    except AssertionError:
        return enter(line)


def my_iter(start, end):
    while start <= end:
        yield start
        start += 1


origin_start = enter("Введите начальное число\n>>>:")
origin_end = enter("Введите конечное число\n>>>:")
print(*list(my_iter(int(origin_start), int(origin_end))))
