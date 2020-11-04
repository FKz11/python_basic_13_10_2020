"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


def m_enter():
    """
            Рекурсивная функция, которая возвращает ввод данных, если ввод был корректным.
         """
    print("Вводите матрицу через пробел построчно, окончанием ввода свидетильствует пустая строка без пробелов:")
    result = []
    try:
        line = input(">>>:").split(' ')
        while line != ['']:
            result.append(line)
            line = input(">>>:").split(' ')
            assert len(line) == len(result[0]) or line == ['']
        return result
    except AssertionError:
        print("Ввод не корректен")
        return m_enter()


class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        matrix_str = ''
        for i in self.m_list:
            matrix_str += f'{i}\n'
        return matrix_str

    def __add__(self, other):
        if len(self.m_list) == len(other.m_list) and len(self.m_list[0]) == len(other.m_list[0]):
            result = Matrix([])
            for i in range(len(self.m_list)):
                result_line = []
                for j in range(len(self.m_list[0])):
                    try:
                        float(self.m_list[i][j] and float(other.m_list[i][j]))
                        result_line.append(float(self.m_list[i][j]) + float(other.m_list[i][j]))
                    except ValueError:
                        result_line.append(f'{self.m_list[i][j]} + {other.m_list[i][j]}')
                result.m_list.append(result_line)
            return result
        raise ValueError('Матрицы не одинакового размера')


if __name__ == "__main__":
    orig_matrix_1 = Matrix(m_enter())
    orig_matrix_2 = Matrix(m_enter())
    orig_matrix_3 = orig_matrix_1 + orig_matrix_2
    print(orig_matrix_3)
