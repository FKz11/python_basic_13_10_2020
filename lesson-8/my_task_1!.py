"""
1. Сократить строку тем, что если 1 символ повторяется многа раз подряд,
то нужно записать его и количество его повторений подряд.
"""


def fun(line: str):
    result = ""
    count = 1
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            count += 1
        else:
            result += line[i]
            if count > 1:
                result += str(count)
            count = 1
    result += line[len(line) - 1]
    if count > 1:
        result += str(count)
    return result


print(fun(input("Введите строку символов\n>>>:")))
