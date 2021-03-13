"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы,
отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class OfficeEquipmentWarehouseDescription:
    @staticmethod
    def description():
        print("Склад оргтехники")


class OfficeEquipment:
    dictionary = {"printer": [], "scanner": [], "xerox": []}
    all_quantity = {"printer": 0, "scanner": 0, "xerox": 0}

    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    @classmethod
    def define(cls, name, cost, quantity, text):
        try:
            float(cost) and float(quantity)
            assert float(quantity) % 1 == 0
            if "printer" in name:
                Printer(name, cost, quantity, text)
            if "scanner" in name:
                Scanner(name, cost, quantity, text)
            if "xerox" in name:
                Xerox(name, cost, quantity, text)
        except ValueError:
            print("Ошибка, стоимость и количество может быть только числом!")
        except AssertionError:
            print("Ошибка, количество может быть только целым числом!")


class Printer(OfficeEquipment):
    def __init__(self, name, cost, quantity, text_printer):
        super().__init__(name, cost, quantity)
        self.text_printer = text_printer
        super().dictionary["printer"].append([name, cost, quantity, text_printer])
        super().all_quantity["printer"] += int(cost)


class Scanner(OfficeEquipment):
    def __init__(self, name, cost, quantity, text_scanner):
        super().__init__(name, cost, quantity)
        self.text_scanner = text_scanner
        super().dictionary["scanner"].append([name, cost, quantity, text_scanner])
        super().all_quantity["printer"] += int(cost)


class Xerox(OfficeEquipment):
    def __init__(self, name, cost, quantity, text_xerox):
        super().__init__(name, cost, quantity)
        self.text_xerox = text_xerox
        super().dictionary["xerox"].append([name, cost, quantity, text_xerox])
        super().all_quantity["printer"] += int(cost)


origin_printer_name = input("Введите имя с содержанием printer/scanner/xerox\n>>>:")
origin_printer_cost = input("Введите цену\n>>>:")
origin_printer_quantity = input("Введите количество\n>>>:")
origin_printer_text_printer = input("Введите текст\n>>>:")
OfficeEquipment.define(origin_printer_name, origin_printer_cost, origin_printer_quantity,
                       origin_printer_text_printer)
print(OfficeEquipment.dictionary)
print(OfficeEquipment.all_quantity)
