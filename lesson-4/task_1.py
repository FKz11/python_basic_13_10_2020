"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотр
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

name, origin_work, origin_rate, origin_prize = argv


def salary(work, rate, prize):
    """
            Функция, которая считает по формуле.
        """
    return work * rate + prize


print(salary(float(origin_work), float(origin_rate), float(origin_prize)))
