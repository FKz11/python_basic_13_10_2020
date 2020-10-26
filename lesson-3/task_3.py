"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def enter(line):
    """
            Рекурсивная функция, которая возвращает ввод данных, если ввод был корректным.
        """
    number = input(line)
    try:
        float(number)
        return number
    except ValueError:
        return enter(line)


def sum_2max(a, b, c):
    """
            Функция суммы двух наибольших аргументов.
        """
    if a >= c and b >= c:
        return a + b
    if a >= b and c >= b:
        return a + c
    if b >= a and c >= a:
        return b + c


number1 = enter("Введите первое число\n>>>:")
number2 = enter("Введите второе число\n>>>:")
number3 = enter("Введите третье число\n>>>:")
print(sum_2max(float(number1), float(number2), float(number3)))
