"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def my_range(length):
    i = 0
    while i < length:
        yield i
        i += 1


def enter(line):
    words = input(line).split(' ')
    try:
        for i in words:
            assert i.isalpha() and i.islower()
        return words
    except AssertionError:
        return enter(line)


def upper_word(word):
    return word[0].upper() + word[1:]


def upper_words(words):
    for i in my_range(len(words)):
        words[i] = upper_word(words[i])
    return words


data = enter("Введите слова из маленьких латинских букв\n>>>:")
print(*upper_words(data))
