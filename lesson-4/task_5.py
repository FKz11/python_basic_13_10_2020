"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


def my_range(start, end):
    """
            Генератор, аналог функции range(), в которую передаётся толька старт и конец.
        """
    while start < end:
        yield start
        start += 1


def my_reduce(func, data):
    """
            Функция, аналог функции reduce().
        """
    while len(data) > 1:
        data = [func(data[0], data[1])] + data[2:]
    return data


print(*my_reduce(lambda x, y: x * y, [a for a in my_range(100, 1001) if not a & 1]))
