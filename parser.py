from util import *
from excel import write_to_excel


def parse_one_page(url: str):
    html_code: str = check_internet_access(url=url)
    articles: list = get_contents_div(html_code=html_code)
    write_to_excel(articles=articles)


if __name__ == '__main__':
    parse_one_page('https://overclockers.ru/lab?offset=0&max=20')
