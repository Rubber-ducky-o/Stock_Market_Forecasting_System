import sqlite3
symbol = 'APPL'

def table_creating_and_insert(date_time,open_price, high, low, close, volume):
    TableName = symbol
    try:
        print('getting database...')
        data_base_file = ('storing_stock_data.db')
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
        f"INSERT OR IGNORE INTO [{TableName}] (DATE, OPEN, HIGH, LOW, CLOSE, VOLUME)"
        f"VALUES (?,?,?,?,?,?),"
        (date_time, open_price, high, low, close, volume)
        )

        connect.commit()
        connect.close()
    except sqlite3.Error as e:
        print(f'Current error: {e}')

    return
