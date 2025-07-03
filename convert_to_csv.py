import sqlite3
import pandas as pd

database = 'storing_stock_data.db'
csv_file = 'stock_data.csv'

try:

    connect = sqlite3.connect(database)
    user = input('Enter the stock:\n')
    df = pd.read_sql_query(f"SELECT * FROM {user}",connect)
    df.to_csv(f'{user}_stock_data.csv', index = False, encoding = 'utf-8')
    connect.close()

except sqlite3.OperationalError:
    print('error')