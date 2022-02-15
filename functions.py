import xlrd


# Счетчик четных чисел в столбце
def counting_even_numbers(col, worksheet):
    # Инициализируем счетчик
    count = 0

    for cell in worksheet.col(col):
        try:
            if not (float(cell.value) % 2):
                count += 1
        except ValueError:
            pass

    print(f'Ответ на вопрос: {worksheet.cell_value(1, 1)}', count)


