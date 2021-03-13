"""
2. Из списка слов сделать список списков, в котором сгруппированы полные анограммы.
"""


def fun(my_list):
    result = []
    for i in my_list:
        anagram = []
        for j in my_list:
            if len(i) == len(j):
                flag = True
                c = 0
                while flag and c < len(i):
                    if i[c] not in j:
                        flag = False
                    c += 1
                w = 0
                while flag and w < len(j):
                    if j[w] not in i:
                        flag = False
                    w += 1
                if flag:
                    anagram.append(j)
        result.append(anagram)
    set_result = []
    for r in result:
        if r not in set_result:
            set_result.append(r)
    return set_result


print(fun(input("Введите слова через пробел\n>>>:").split(' ')))
