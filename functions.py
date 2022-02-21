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
def counting_Tuesdays(col, worksheet, day_week=None):
    # Инициализируем счетчик
    count = 0
    # Проверяем есть ли название столбца
    if day_week != None:
        for cell in worksheet.col(col):
            # Берем первое значение из ячейки (название дня недели)
            if day_week == cell.value.split()[0]:
                count += 1
    else:
        for cell in worksheet.col(col):
            try:
                # Берем первое значение из ячейки разделяем на год-месяц-день
                date = cell.value.split()[0].split('-')
                if day_of_week(date[2], date[1], date[0]) == 'Tue':
                    count += 1
            except IndexError:
                pass

    print(f'Ответ на вопрос: {worksheet.cell_value(1, col)} ({worksheet.cell_value(0, col)})', count)


# Счетчик вторников черз datetime и calendar
def counting_Tuesdays2(col, worksheet):
    # Инициализируем счетчик
    count = 0

    for cell in worksheet.col(col):
        date = cell.value.split()[0]
        if day_of_week2(date) == 'Tuesday':
            count += 1

    print(f'Ответ на вопрос: {worksheet.cell_value(1, col)} ({worksheet.cell_value(0, col)})', count)


# Счетчик последних вторников
def counting_last_Tuesdays(col, worksheet):
    # Инициализируем счетчик
    count = 0

    for cell in worksheet.col(col):
        try:
            # Берем первое значение из ячейки разделяем на год-месяц-день
            date = cell.value.split()[0].split('-')
            # Преобразуем дату в iso формат
            date_ = f'{date[2]}-{date[0]}-{date[1]}'
            if day_of_week2(date_) == 'Tuesday':
                # Прибовляем еще 7 дней
                date[1] = int(date[1]) + 7
                # Приводим день к формату ДД
                if not (date[1] // 10):
                    date[1] = '0' + str(date[1])
                date_ = f'{date[2]}-{date[0]}-{date[1]}'
                # Проверка следующий вторник или нет
                if day_of_week2(date_) != 'Tuesday':
                    count += 1
        except IndexError:
            pass

    print(f'Ответ на вопрос: {worksheet.cell_value(1, col)} ({worksheet.cell_value(0, col)})', count)
    

# Счетчик последних вторников вариант 2
def counting_last_Tuesdays2(col, worksheet):
    # Инициализируем счетчик
    count = 0

    for cell in worksheet.col(col):
        try:
            # Берем первое значение из ячейки разделяем на год-месяц-день
            date = cell.value.split()[0].split('-')
            # Преобразуем дату в iso формат
            date_ = f'{date[2]}-{date[0]}-{date[1]}'
            if day_of_week2(date_) == 'Tuesday':
                # Прибовляем еще 7 дней
                date[1] = int(date[1]) + 7
                # Приводим день к формату ДД
                if not(date[1]//10):
                    date[1] = '0' + str(date[1])
                date_ = f'{date[2]}-{date[0]}-{date[1]}'
                # Проверка следующий вторник или нет
                if day_of_week2(date_) != 'Tuesday':
                    count += 1
        except IndexError:
            pass

    print(f'Ответ на вопрос: {worksheet.cell_value(1, col)} ({worksheet.cell_value(0, col)})', count)