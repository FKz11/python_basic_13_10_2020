"""
4. Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


def enter(line):
    numbers = input(line).split(' ')
    try:
        for i in numbers:
            float(i)
        return numbers
    except ValueError:
        return enter(line)


my_list = enter("Введите числа через пробел\n>>>:")
new_list = [a for a in my_list if a not in (my_list[:my_list.index(a)] + my_list[my_list.index(a)+1:])]
print(*new_list)
