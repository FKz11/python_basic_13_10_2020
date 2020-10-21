"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def enter(line):
    number = input(line)
    try:
        float(number)
        if line == "Введите делитель\n>>>:":
            assert float(number) != 0
        return number
    except ValueError:
        return enter(line)
    except AssertionError:
        return enter(line)


def division(a, b):
    return a / b


divisible = enter("Введите делимое\n>>>:")
divisor = enter("Введите делитель\n>>>:")
print(division(float(divisible), float(divisor)))
