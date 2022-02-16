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