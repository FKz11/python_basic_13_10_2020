"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def enter(line):
    """
            Рекурсивная функция, которая возвращает ввод данных, если ввод был корректным.
        """
    argument = input(line)
    try:
        if line == "Введите год рождения\n>>>:":
            assert argument.isdigit() and int(argument) < 2021
        return argument
    except AssertionError:
        return enter(line)


def data(name, surname, year_of_birth, city_of_residence, email, phone_number):
    """
            Функция возвращающая отформатированные данные.
        """
    return f'{name}, {surname}, {year_of_birth}, {city_of_residence}, {email}, {phone_number}'


original_name = input("Введите имя\n>>>:")
original_surname = input("Введите фамилию\n>>>:")
original_year_of_birth = enter("Введите год рождения\n>>>:")
original_city_of_residence = input("Введите город проживания\n>>>:")
original_email = input("Введите email\n>>>:")
original_phone_number = input("Введите телефон\n>>>:")
print(data(
    name=original_name,
    surname=original_surname,
    year_of_birth=original_year_of_birth,
    city_of_residence=original_city_of_residence,
    email=original_email,
    phone_number=original_phone_number
))
