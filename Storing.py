import sqlite3
from pathlib import Path

def table_creating_and_insert(SYMBOL,date_time,open_price, high, low, close, volume):
    TableName = SYMBOL
    folder_name = Path('stored_stock_data')

    try:
        print('getting database...')
        data_base_file = folder_name / ('storing_stock_data.db')
        connect = sqlite3.connect(data_base_file)
        print('connect')
        cursor = connect.cursor()
        print('cursor')
        table_create = (
            f"CREATE TABLE IF NOT EXISTS [{TableName}] ("
            f"DATE UNIQUE PRIMARY KEY,"
            f"OPEN, "
            f"HIGH, "
            f"LOW, "
            f"CLOSE, "
            f"VOLUME, "
            f"DIVIDEND_AMOUNT, "
            f"SPLIT_COEFFICIENT) "
        )
        cursor.execute(table_create)
        print('table created/found successfully')

        cursor.execute(
        f"INSERT OR IGNORE INTO [{TableName}] "
        f"(DATE, OPEN, HIGH, LOW, CLOSE, VOLUME)"
        f"VALUES (?,?,?,?,?,?)",
        (date_time, open_price, high, low, close, volume)
        )

        connect.commit()
        connect.close()


    except sqlite3.Error as e:
        print(f'Current error: {e}')

    return
