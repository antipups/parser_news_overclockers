import eel
from util import *
from excel import write_to_excel
from os import startfile
from database import add_to_db


articles, category = [], ''


def parse_one_page(url: str):
    """
        Парс першу сторінку
    :param url:
    :return:
    """
    if not check_url(url=url):
        return 'Посилання має містити в собі максиму статей'
    html_code: str = check_internet_access(url=url)     # перевіряємо доступ до сайту
    if not html_code:
        return 'Немає доступу до сайту'
    else:
        global articles, category
        articles, category = get_contents_div(html_code=html_code), get_category(html_code=html_code)
        add_to_db(articles)
        return convert_into_table(articles=articles,
                                  category=category)


@eel.expose     # вказуємо доступ з html
def parse(url: str):
    # url = 'https://overclockers.ru/lab?offset=-180&max=200'
    return parse_one_page(url)


@eel.expose     # вказуємо доступ з html
def write_to_xlsx():
    global category, category
    if write_to_excel(articles=articles,
                      category=category):
        return "Дані успішно записані"
    else:
        return "Помилка запису, закрийте excel"


@eel.expose
def open_xlsx():
    startfile(RESULT_FILENAME)


if __name__ == '__main__':
    eel.init('web_folder')  # вказуємо з якої папки брати веб файли
    eel.start('index.html', cmdline_args=['--start-fullscreen'])   # вказуємо запуск програми в повний екран
