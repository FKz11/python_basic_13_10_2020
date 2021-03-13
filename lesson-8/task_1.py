"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    cls_list_date = ''

    def __init__(self, list_date):
        self.list_date = list_date
        Date.cls_list_date = list_date

    @classmethod
    def format(cls):
        return [int(a) for a in cls.cls_list_date.split('-')]

    @staticmethod
    def validation():
        data = Date.cls_list_date.split('-')
        if len(data) != 3:
            print("Не правильная форма записи!")
        else:
            try:
                int(data[0]) and int(data[1]) and int(data[2])
                assert int(data[0]) % 1 == 0 and int(data[1]) % 1 == 0 \
                       and int(data[2]) % 1 == 0 and 12 >= int(data[1]) >= 1 \
                       and 1 <= int(data[0]) <= 31 and int(data[2]) >= 0
            except ValueError:
                print("Введины не числа")
            except AssertionError:
                print("Невозможные значения!")


origin_date = Date(input("Введите дату в формате день-месяц-год\n>>>:"))
origin_date.validation()
print(*Date.format())
