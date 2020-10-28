"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('task_3_read.txt', 'r', encoding='UTF=8') as file:
    max_20000 = []
    my_sum = 0
    quantity = 0
    for lines in file.readlines():
        data = lines.split(' ')
        my_sum += float(data[1])
        quantity += 1
        if float(data[1]) < 20000:
            max_20000.append(data[0])
    print("Меньше 20000:", end=' ')
    print(*max_20000, sep=', ')
    print("Среднее:", my_sum / quantity)
