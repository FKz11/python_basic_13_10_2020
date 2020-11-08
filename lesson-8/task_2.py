"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision:
    def __init__(self, arithmetic):
        try:
            self.result = str(eval(arithmetic))
        except ZeroDivisionError:
            self.result = "ZeroDivisionError"
            print("Ошибка. Произошло деление на ноль!")


origin_arithmetic = ZeroDivision(input("Введите арефметическое выражение\n>>>:"))
print(origin_arithmetic.result)
