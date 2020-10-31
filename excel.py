from openpyxl import Workbook
from config import RESULT_FILENAME, COLUMN_SIZE, TITLE_COLUMNS


def setup_new_workbook() -> Workbook:
    """
        Попереднє налаштування вивідного Ексель файлу, а саме:
        збільшення колонок;
        додаємо назви колонок до стовпчиків;
        та інше
    :return:
    """
    workbook: Workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Статьи'
    for index, column in enumerate(COLUMN_SIZE):
        sheet.column_dimensions[chr(65 + index)].width = column
    sheet.append(TITLE_COLUMNS)
    return workbook


def write_to_excel(articles: list) -> bool:
    """
        запис даних статей в файл
    :param articles:
    :return:
    """
    workbook: Workbook = setup_new_workbook()
    for article in articles:
        workbook.active.append(article)
    try:
        workbook.save(RESULT_FILENAME)
    except PermissionError:     # якщо файл використовується його не можна перезаписати
        return False
    else:
        return True


if __name__ == '__main__':
    pass