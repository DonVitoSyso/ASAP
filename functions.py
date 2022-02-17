import xlrd
from utils import *


# Счетчик четных чисел в столбце
def counting_even_numbers(col, worksheet):
    # Инициализируем счетчик
    count = 0

    for cell in worksheet.col(col):
        try:
            if not (int(cell.value) % 2):
                count += 1
        except ValueError:
            pass

    print(f'Ответ на вопрос: {worksheet.cell_value(1, col)}', count)


# Счетчик простых чисел в столбце
def counting_prime_numbers(col, worksheet):
    # Инициализируем счетчик
    count = 0

    for cell in worksheet.col(col):
        try:
            if not (even_numbers(int(cell.value))):
                count += 1
        except ValueError:
            pass

    print(f'Ответ на вопрос: {worksheet.cell_value(1, col)}', count)


# Счетчик чисел меньше чем заданное
def counting_number_less(col, worksheet, number):
    # Инициализируем счетчик
    count = 0

    for cell in worksheet.col(col):
        try:
            # Избавимся от всех пробелов в строках-числах
            cell.value = "".join(cell.value.split())
            # Приведем все числа к общему формату - через "."
            cell.value = ".".join(cell.value.split(','))
            if float(cell.value) < number:
                count += 1
        except ValueError:
            pass

    print(f'Ответ на вопрос: {worksheet.cell_value(1, col)}', count)


# Счетчик вторников
def counting_Tuesdays(col, worksheet, number):
    pass
