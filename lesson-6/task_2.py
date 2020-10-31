"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


def enter(line):
    """
            Рекурсивная функция, которая возвращает ввод данных, если ввод был корректным.
         """
    number = input(line)
    try:
        assert float(number) > 0
        return number
    except ValueError:
        return enter(line)
    except AssertionError:
        return enter(line)


class Road:
    _weight = 25
    _thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_asphalt(self):
        return self._length * self._width * self._weight * self._thickness / 1000


original_length = enter("Введите длину в м\n>>>:")
original_width = enter("Введите ширину в м\n>>>:")
original_road = Road(float(original_length), float(original_width))
print(str(original_road.weight_of_asphalt()) + ' т')
