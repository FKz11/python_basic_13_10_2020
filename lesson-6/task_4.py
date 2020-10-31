"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


def enter(line):
    """
            Рекурсивная функция, которая возвращает ввод данных, если ввод был корректным.
         """
    text = input(line)
    try:
        if line == "Введите скорость\n>>>:":
            float(text)
            return text
        if line == "Это полиция? да/нет\n>>>:":
            if text == 'да' or text == 'Да' or text == 'ДА':
                return True
            if text == 'нет' or text == 'Нет' or text == 'НЕТ':
                return False
            return enter(line)
    except ValueError:
        return enter(line)


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if float(self.speed) > 60:
            print(f'Скорость {self.speed}. Превышение скорости!!!!')
        else:
            print(f'Скорость {self.speed}')


class SportCar(Car):
    def signal(self):
        print('Vrrrrrrrr')


class WorkCar(Car):
    def show_speed(self):
        if float(self.speed) > 40:
            print(f'Скорость {self.speed}. Превышение скорости!!!!')
        else:
            print(f'Скорость {self.speed}')


class PoliceCar(Car):
    def signal(self):
        print('Uiuiuiuiu')


print("У вас рабочая машина")
origin_speed = enter("Введите скорость\n>>>:")
origin_color = input("Введите цвет\n>>>:")
origin_name = input("Введите имя\n>>>:")
origin_is_police = enter("Это полиция? да/нет\n>>>:")
origin_car = WorkCar(origin_speed, origin_color, origin_name, origin_is_police)
print(origin_car.name)
origin_car.go()
origin_car.turn(input("Куда повернуть?\n>>>:"))
origin_car.show_speed()
origin_car.stop()
