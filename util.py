from typing import List

from config import *
from requests import get, Response
import re


def check_internet_access(url: str) -> str:
    """
        отримання інтернет сторінки якщо це можливо з
        виловом всіх помилок (немає інтернету і інших)
    :param url:
    :return:
    """
    try:
        request: Response = get(url=url,
                                headers=REQUEST_HEADERS)
    except:     # якщо сталася помилка
        return ''
    else:
        if not request.ok:  # якщо сайт не видав дані
            return ''
        else:
            html: str = request.text
            return html


def get_divs(html_code: str) -> tuple:
    """
        Для відбору потрібних Дивов з потрібною нам інформацією (автором, датою і іншим)
    :param html_code:
    :return:
    """
    contents_div = re.finditer(pattern='<div class=\"content\">((?!/div).)*',
                               string=html_code,
                               flags=re.DOTALL)
    return tuple(contents_div)[:MAX_ARTICLES_ON_PAGE]


def get_url(html_code: str) -> str:
    result = re.search(pattern=r'href=\"[^\"]*',
                       string=html_code).group()[6:]
    return 'https://overclockers.ru' + result


def get_title(html_code: str) -> str:
    return re.search(pattern=r'header\">[^<]*',
                     string=html_code).group()[8:].strip()


def get_author(html_code: str) -> str:
    return re.search(pattern=r'author">[^<]*',
                     string=html_code).group()[8:].strip()


def get_date(html_code: str) -> str:
    return re.search(pattern=r'date\">[^<]*',
                     string=html_code).group()[6:].strip()


def get_contents_div(html_code: str) -> List[tuple]:
    """
        Отримуємо інформацію з потрібної сторінки, а саме
        - Дата створення;
        - Автор;
        - Назва;
        - Посилання на статтю.
    :param html_code:
    :return:
    """
    cut_funtions: tuple = (get_url, get_title, get_author, get_date)
    articles_data: list = []    # всі результати з статей будуть тут
    for div in get_divs(html_code):
        articles_data.append(tuple(func(div.group()) for func in cut_funtions))
    return articles_data


def convert_into_table(articles: list):
    """
        генерація таблиці для html
    :param articles:
    :return:
    """
    result = '<table border=1>'
    for article in articles:
        result += f'<tr><td><a href="{article[0]}">' + '</td><td>'.join(article[1:]) + '</td></a></tr>'
    return result + '</table>'
