from functions import *


# Открываем файл task_support
workbook = xlrd.open_workbook("task_support.xlsx")
# Указываем нужный лист
worksheet = workbook.sheet_by_index(1)

# Пройдемся по столбцу 2 и посчитаем все четные числа
counting_even_numbers(1, worksheet)
# Пройдемся по столбцу 3 и посчитаем простые числа
counting_prime_numbers(2, worksheet)
