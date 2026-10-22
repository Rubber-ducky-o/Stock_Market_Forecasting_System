import pandas as pd
from pathlib import Path
from statsmodels.tsa.arima.model import ARIMA

def ARIMA_Model(symbol):
    try:
        file_name = f'{symbol}_stock_data.csv'
        path = Path(file_name).resolve()

        df = pd.read_csv(path, parse_dates=['DATE'])
        df = df.set_index('DATE')

        series = df['CLOSE'].asfreq('5min').ffill().bfill()
        arimaa = ARIMA(series, order = (1,1,1))
        fit = arimaa.fit()

        print(fit.summary())
        future = fit.get_forecast(steps=10)
        print('Forecasted:\n', future.predicted_mean)
        print('95% confidence interval:\n', future.conf_int())
    except Exception as e:
        print(f'This error occured {e}')




