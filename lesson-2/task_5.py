"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""


def enter(line):
    number = input(line)
    try:
        assert number.isdigit() and int(number) != 0
        return number
    except AssertionError:
        return enter(line)


quantity = enter("Введите количество новых элементов рейтинга\n>>>: ")
rating = [7, 5, 3, 3, 2]
for i in range(int(quantity)):
    position = enter("Введите новый элемент рейтинга\n>>>: ")
    new_rating = []
    flag = True
    for element in rating:
        if int(position) > element and flag:
            new_rating.append(int(position))
            flag = False
        new_rating.append(element)
    if flag:
        new_rating.append(int(position))
    rating = new_rating
print(rating)
