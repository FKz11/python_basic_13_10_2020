"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
"""


def enter(line):
    number = input(line)
    try:
        assert number.isdigit()
        return number
    except AssertionError:
        return enter(line)


quantity_title = enter("Введите количество разделов\n>>>: ")
product = []
score = 0
for i in range(int(quantity_title)):
    title = input("Введите название товара\n>>>: ")
    price = input("Введите цену товара\n>>>: ")
    quantity = enter("Введите количество товара\n>>>: ")
    unit = input("Введите единицу измерения товара\n>>>: ")
    score += 1
    product.append((score, {"название": title, "цена": price, "количество": quantity, "eд": unit}))
product_analytics = {"название": [], "цена": [], "количество": [], "eд": []}
for i in range(int(quantity_title)):
    product_analytics["название"].append(product[i][1]["название"])
    product_analytics["цена"].append(product[i][1]["цена"])
    product_analytics["количество"].append(product[i][1]["количество"])
    product_analytics["eд"].append(product[i][1]["eд"])
if len(set(product_analytics["eд"])) == 1:
    product_analytics["eд"] = set(product_analytics["eд"])
print(product_analytics)
