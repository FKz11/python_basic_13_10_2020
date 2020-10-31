"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


def enter(line):
    """
            Рекурсивная функция, которая возвращает ввод данных, если ввод был корректным.
         """
    number = input(line)
    try:
        assert float(number) >= 0
        return number
    except ValueError:
        return enter(line)
    except AssertionError:
        return enter(line)


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


origin_name = input("Введите имя\n>>>:")
origin_surname = input("Введите фамилию\n>>>:")
origin_position = input("Введите должность\n>>>:")
origin_wage = enter("Введите оклад\n>>>:")
origin_bonus = enter("Введите премию\n>>>:")
employee = Position(origin_name, origin_surname, origin_position, float(origin_wage), float(origin_bonus))
print(employee.get_full_name())
print(employee.get_total_income())
