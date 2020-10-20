"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number = input("Введите число\n>>>: ")
degree_10 = 0
max_number = 0
while int(number) // 10**degree_10 != 0:
    if max_number < (int(number) % 10**(degree_10+1)) // 10**degree_10:
        max_number = (int(number) % 10**(degree_10+1)) // 10**degree_10
    degree_10 += 1
print("Максимальная цифра в числе: " + str(max_number))
