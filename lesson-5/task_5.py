"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def sum_list(my_list):
    my_sum = 0
    for i in my_list:
        my_sum += float(i)
    return my_sum


with open('task_5_write_read.txt', 'w', encoding='UTF=8') as file_w:
    file_w.write("1 2 4 2 8 9 3 10 4 2 4\n")
with open('task_5_write_read.txt', 'r', encoding='UTF=8') as file_r:
    data = file_r.read().split(' ')
    print(sum_list(data))
