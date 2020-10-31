from util import *


def parse_one_page(url: str):
    check_internet_access(url=url)


if __name__ == '__main__':
    parse_one_page('https://overclockers.ru/lab?offset=-180&max=200')
