from config import *
from requests import get, Response


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
