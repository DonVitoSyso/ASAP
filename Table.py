from functions import *


# Открываем файл task_support
workbook = xlrd.open_workbook("task_support.xlsx")
# Указываем нужный лист
worksheet = workbook.sheet_by_index(1)

# Номер столбца, тк столбцы по порядку - указываем начальный
col = 0

# Пройдемся по столбцу 2 и посчитаем все четные числа
counting_even_numbers(col+1, worksheet)
# Пройдемся по столбцу 3 и посчитаем простые числа
counting_prime_numbers(col+2, worksheet)
# Пройдемся по столбцу 4 и посчитаем числа меньше 0.5
counting_number_less(col+3, worksheet, 0.5)
# Пройдемся по столбцу 5 и посчитаем число вторников
counting_Tuesdays(col+4, worksheet, 'Thu')
# Пройдемся по столбцу 6 и посчитаем число вторников
counting_Tuesdays(col+5, worksheet, 'Thu')