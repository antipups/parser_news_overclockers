from sqlite3 import Connection
from config import DB_FILENAME


def add_to_db(articles: list):
    connect = Connection(DB_FILENAME)
    cursor = connect.cursor()
    for article in articles:
        # print(article)
        values_string = '"' + '", "'.join(article) + '"'    # генеруємо рядок для запиту
        query = 'INSERT INTO articles ' \
                f'VALUES ({values_string})'
        cursor.execute(query)
    connect.commit()
    connect.close()
