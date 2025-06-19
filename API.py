import requests
import api_key
import json
import sqlite3
import pandas as pd

symbol = 'AAPL'


def get_get_stock():
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key.API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(data)

    data_base_file = ('storing_stock_data.db')
    try:
        TableName = symbol
        connect = sqlite3.connect(data_base_file)
        cursor = connect.cursor()
        table_create = (f"CREATE TABLE [{TableName}]("
                        f"DATE UNIQUE PRIMARY KEY,"
                        f"OPEN,"
                        f"HIGH,"
                        f"LOW,"
                        f"CLOSE,"
                        f"VOLUME)")

        cursor.execute(table_create)
    except sqlite3.Error as error:
            print('Error while connecting to sqlite database', error)

get_get_stock()


