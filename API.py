import requests
import json
import sqlite3
import Storing

symbol = 'AAPL'


def get_get_stock(symbol):
    try:
        #url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key.API_KEY}'
        '''
        TESTING URL:
        '''
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo'

        response = requests.get(url)
        print('requesting data')

        if response.status_code == 200:
            print('data retrieved')
            data = json.loads(response.text)
            if 'Time Series (5min)' in data:
                time_series = data['Time Series (5min)']
            for time, value in time_series.items():
                date_time = value['None']
                open_price = value['1. open']
                high = value['2. high']
                low = value['3. low']
                close = value['4. close']
                volume = value['5. volume']
                Storing.storing(date_time,open_price, high, low, close, volume)

        elif response.status_code != 200:
            print('Error occured not sure where but not retrieving data')


    except Exception as e:
        print(f'Current error from {e}')
    except sqlite3.OperationalError:
        print('OperationalError occured')
    except sqlite3.Error:
        print('Error occured')



get_get_stock()


