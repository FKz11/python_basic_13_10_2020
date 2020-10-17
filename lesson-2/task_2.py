"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""


def enter(line):
    number = input(line)
    try:
        assert number.isdigit()
        return number
    except AssertionError:
        return enter(line)


length = enter("Введите количество значений\n>>>: ")
list_values = []
for i in range(int(length)):
    list_values .append(input("Введите зачение\n>>>: "))
for i in range(0, int(length) // 2 * 2, 2):
    list_values[i], list_values[i + 1] = list_values[i + 1], list_values[i]
print(list_values)
