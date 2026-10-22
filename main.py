import API
import Stored_data
import arima_model
import convert_to_csv
import argparse


def main():
    try:
        parser = argparse.ArgumentParser(
            prog = 'main'
            description = 'Automatic '
        )
        Stored_data.creating_folder()
        API.get_get_stock(symbol)
        convert_to_csv.convert_to_csv()
        arima_model.ARIMA_Model(symbol)


    except Exception as e:
        print(e)








if __name__ == '__main__':
    main()