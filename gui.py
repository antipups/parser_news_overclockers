import eel
from util import *
from excel import write_to_excel


articles = []


def parse_one_page(url: str):
    """
        Парс першу сторінку
    :param url:
    :return:
    """
    html_code: str = check_internet_access(url=url)     # перевіряємо доступ до сайту
    if not html_code:
        return 'Немає доступу до сайту'
    else:
        global articles
        articles = get_contents_div(html_code=html_code)
        return convert_into_table(articles)


@eel.expose     # вказуємо доступ з html
def parse():
    return parse_one_page('https://overclockers.ru/lab?offset=-180&max=200')


@eel.expose     # вказуємо доступ з html
def write_to_xlsx():
    global articles
    write_to_excel(articles=articles)


if __name__ == '__main__':
    eel.init('web_folder')  # вказуємо з якої папки брати веб файли
    eel.start('index.html', cmdline_args=['--start-fullscreen'])   # вказуємо запуск програми в повний екран
