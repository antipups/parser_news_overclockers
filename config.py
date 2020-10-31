REQUEST_HEADERS = {
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}

URL = 'https://overclockers.ru/lab?offset=-180&max=200'

MAX_ARTICLES_ON_PAGE = 200

RESULT_FILENAME = 'result.xlsx'
COLUMN_SIZE = (150,
               100,
               20,
               20)
TITLE_COLUMNS = ('Ссылка',
                 'Название',
                 'Автор',
                 'Дата создания')
