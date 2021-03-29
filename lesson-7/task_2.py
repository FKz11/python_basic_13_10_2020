"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


def enter(line):
    """
            Рекурсивная функция, которая создает элементы класса, если ввод был корректным.
         """
    try:
        data = input(line).split(' ')
        assert len(data) == 2 or data == ['']
        while data != ['']:
            float(data[1])
            if line == "Введите пальто в формате (название размер), окончанием ввода свидетильствует пустая строка без пробелов\n>>>:":
                Coat(data)
            if line == "Введите костюмы в формате (название рост), окончанием ввода свидетильствует пустая строка без пробелов\n>>>:":
                Suit(data)
            data = input(line).split(' ')
            assert len(data) == 2 or data == ['']
    except ValueError:
        print("Ввод не корректен")
        return enter(line)
    except AssertionError:
        print("Ввод не корректен")
        return enter(line)


class Clothes:
    coat_expenditure_list = []
    suit_expenditure_list = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def all_expenditure(cls):
        return sum(cls.coat_expenditure_list) + sum(cls.suit_expenditure_list)


class Coat(Clothes):
    def __init__(self, name_size):
        self.size = name_size[1]
        super().__init__(name_size[0])
        super().coat_expenditure_list.append(self.coat_expenditure)

    @property
    def coat_expenditure(self):
        return float(self.size) / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name_height):
        self.height = name_height[1]
        super().__init__(name_height[0])
        super().suit_expenditure_list.append(self.suit_expenditure)

    @property
    def suit_expenditure(self):
        return 2 * float(self.height) + 0.3


if __name__ == "__main__":
    enter(
        "Введите пальто в формате (название размер), окончанием ввода свидетильствует пустая строка без пробелов\n>>>:")
    enter(
        "Введите костюмы в формате (название рост), окончанием ввода свидетильствует пустая строка без пробелов\n>>>:")
    print(Clothes.all_expenditure())
