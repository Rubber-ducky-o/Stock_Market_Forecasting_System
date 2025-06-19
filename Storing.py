import sqlite3
symbol = 'APPL'

data_base_file = ('storing_stock_data.db')
def table_creating():
    try:
        TableName = symbol
        connect = sqlite3.connect(data_base_file)
        cursor = connect.cursor()
        table_create = (f"CREATE TABLE [{TableName}]("
                        f"SYMBOL TEXT PRIMARY KEY,"
                        f"DATE UNIQUE,"
                        f"OPEN,"
                        f"HIGH,"
                         f"LOW,"
                        f"CLOSE,"
                        f"VOLUME)")

        cursor.execute(table_create)
        print('table Created')
    except Exception as e:
        f'Error {e}'

table_creating()