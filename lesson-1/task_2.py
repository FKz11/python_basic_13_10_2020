"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
seconds = input("Введите время в секундах\n>>>: ")
hh_int = int(seconds)//3600
if hh_int < 10:
    hh_str = '0' + str(hh_int)
else:
    hh_str = str(hh_int)
mm_int = (int(seconds) % 3600)//60
if mm_int < 10:
    mm_str = '0' + str(mm_int)
else:
    mm_str = str(mm_int)
ss_int = (int(seconds) % 3600) % 60
if hh_int < 10:
    ss_str = '0' + str(ss_int)
else:
    ss_str = str(ss_int)
seconds_format = f"{hh_str}:{mm_str}:{ss_str}"
print("Время в формате чч:мм:сс: "+seconds_format)
