"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def enter(line):
    """
            Рекурсивная функция, которая возвращает ввод данных, если ввод был корректным.
        """
    number = input(line)
    try:
        assert float(number) % 1 == 0 and float(number) > 0
        return number
    except ValueError:
        return enter(line)
    except AssertionError:
        return enter(line)


def my_range(start, end):
    """
            Генератор, аналог функции range(), в которую передаётся толька старт и конец.
        """
    while start < end:
        yield start
        start += 1


def factorial(end):
    """
            Генератор, который принимает конец n и выдаёт факториалы  1! ... n!
        """
    for i in my_range(1, end + 1):
        result = 1
        for j in my_range(1, i + 1):
            result *= j
        yield result


def factorial_list(end):
    """
            Генератор, перебирающий факториалы 1! ... n!
        """
    for i in factorial(end):
        yield i


origin_end = enter("Введите число\n>>>:")
print(*list(factorial_list(int(origin_end))))
