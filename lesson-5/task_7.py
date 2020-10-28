"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

with open('task_7_read.txt', 'r', encoding='UTF=8') as file_r:
    profit = dict()
    all_profit = 0
    quantity = 0
    for lines in file_r.readlines():
        data = lines.split(' ')
        subtraction = float(data[2]) - float(data[3])
        profit[data[0]] = subtraction
        if subtraction > 0:
            all_profit += subtraction
            quantity += 1
    my_list = [profit, {"average_profit": all_profit / quantity}]
with open('task_7_write.json', 'w', encoding='UTF=8') as file_w:
    json.dump(my_list, file_w)
