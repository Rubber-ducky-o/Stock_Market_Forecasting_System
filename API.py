import requests
import json
import sqlite3
import Storing
import api_key




def get_get_stock(symbol):
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key.API_KEY}'
        '''
        TESTING URL:
        
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo'
        '''
        response = requests.get(url)
        print('requesting data')

        if response.status_code == 200:
            print('data retrieved')
            data = json.loads(response.text)

            time_series = data.get('Time Series (5min)',{})

            if not time_series:
                raise ValueError('No time series in data')

            for date_time, value in time_series.items():
                open_price = value['1. open']
                high = value['2. high']
                low = value['3. low']
                close = value['4. close']
                volume = value['5. volume']
                Storing.table_creating_and_insert(symbol,date_time,open_price, high, low, close, volume)

        elif response.status_code != 200:
            print('Error occured not sure where but not retrieving data')


    except Exception as e:
        print(f'Current error from {e}')
    except sqlite3.OperationalError:
        print('OperationalError occured')






