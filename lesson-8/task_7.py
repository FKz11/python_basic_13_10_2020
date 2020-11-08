"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


def enter(line):
    data = input(line).split('+')
    try:
        assert len(data) == 2
        float(data[0]) and float(data[1][:-1])
        return data
    except AssertionError:
        print("Неправильный формат ввода!")
        return enter(line)
    except ValueError:
        print("Введены не числа!")
        return enter(line)


class ComplexNumber:
    def __init__(self, number):
        self.real_number = float(number[0])
        self.imaginary_number = float(number[1][:-1])

    def __add__(self, other):
        result = ComplexNumber(["0", "0i"])
        result.real_number = self.real_number + other.real_number
        result.imaginary_number = self.imaginary_number + other.imaginary_number
        return result

    def __mul__(self, other):
        result = ComplexNumber(["0", "0i"])
        result.real_number = self.real_number * other.real_number - self.imaginary_number * other.imaginary_number
        result.imaginary_number = self.real_number * other.imaginary_number + self.imaginary_number * other.real_number
        return result

    def __str__(self):
        return f'{self.real_number}+{self.imaginary_number}i'


origin_complex_number_1 = ComplexNumber(enter("Введите комплексное число\n>>>:"))
origin_complex_number_2 = ComplexNumber(enter("Введите комплексное число\n>>>:"))
print(origin_complex_number_1 + origin_complex_number_2)
print(origin_complex_number_1 * origin_complex_number_2)
