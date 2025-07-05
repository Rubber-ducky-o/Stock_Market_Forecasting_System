import sqlite3
import pandas as pd
from pathlib import Path
import os

def convert_to_csv():
    database = 'storing_stock_data.db'
    csv_file = 'stock_data.csv'

    try:

        connect = sqlite3.connect(database)
        user = input('Enter the stock:\n')
        file = f'{user}_stock_data.csv'
        pathing = Path(file)
        if pathing.exists():
            user = input('would you like to delete the current csv file? (Y/N)')
            if user == 'Y':
                os.remove(file)
            elif user == 'N':
                pass

        df = pd.read_sql_query(f"SELECT * FROM {user}",connect)
        df.to_csv(f'{user}_stock_data.csv', index = False, encoding = 'utf-8')
        connect.close()

    except sqlite3.OperationalError:
        print('error')