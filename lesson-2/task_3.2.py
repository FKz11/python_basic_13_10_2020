"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
# Решение через list:


def enter(line):
    number = input(line)
    try:
        assert number.isdigit() and int(number) < 13 and int(number) != 0
        return number
    except AssertionError:
        return enter(line)


month = enter("Введите число месяца\n>>>: ")
list_month = [
    1, "winter",
    2, "winter",
    3, "spring",
    4, "spring",
    5, "spring",
    6, "summer",
    7, "summer",
    8, "summer",
    9, "autumn",
    10, "autumn",
    11, "autumn",
    12, "winter"
]
print(list_month[list_month.index(int(month)) + 1])
