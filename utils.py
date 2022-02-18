from datetime import date
import calendar


# Прописываем статические значения кода месяца для каждого месяца
code_month = {
    1: 1, 2: 4, 3: 4, 4: 0,
    5: 2, 6: 5, 7: 0, 8: 3,
    9: 6, 10: 1, 11: 4, 12: 6,
}
# Прописываем статические значения кода дней недели каждого дня недели
# Старт отсчёта — выходные, то есть: 0 — суббота, 1 — воскресенье и так далее.
week = {
    0: 'Sat', 1: 'Sun', 2: 'Mon', 3: 'Tue',
    4: 'Wed', 5: 'Thu', 6: 'Fri',
}


def even_numbers(num):
    # 0, 1 - не относится к простому числу (в исключение его)
    if num == 1 or num == 0:
        return True
    # Перебираем все возможные делители от 2
    # до половины от числа, которое проверяем
    for i in range(1, num//2):
        # Если число делиться на делитель закончим проверку
        if num%(i+1) == 0:
            return True

# Определение Високо́сного года
def leap_year(year):
    if (year % 4 == 0) and ((year % 400 == 0) or (year % 100 != 0)):
        return True
    else:
        return False

# Определение дня недели
# Формула взята с ресурса https://lifehacker.ru/kakoj-den-nedeli/
def day_of_week(day, month, year):
    # Переведем все в тип int
    day = int(day)
    month = int(month)
    year = int(year)

    # У года берем только последние 2 числа
    last_digit = int(str(year)[-2:])
    # Определяем высокосный год. Высчитываем только 2 первых мес
    # С вычетом еденицы (корректировка на высокосный год)
    if leap_year(year) and (month == 1 or month == 2):
        # Формула для определения дня недел
        code_year = (5 + last_digit + int(last_digit / 4)) % 7
    else:
        # Формула для определения дня недел
        code_year = (6 + last_digit + int(last_digit / 4)) % 7
    return week[(day + code_month[month] + code_year) % 7]

# Второй вариант расчета даты
def day_of_week2(date_):
    try:
        my_date = date.fromisoformat(date_)
        return calendar.day_name[my_date.weekday()]
    except ValueError:
        pass
