import logic
import API
import Storing
import Stored_data
import arima_model
import convert_to_csv
def main():
    try:
        symbol  = input('Please input the company stock you\'d like to check:\n')
        Stored_data.creating_folder()
        API.get_get_stock(symbol)
        convert_to_csv.convert_to_csv()
        arima_model.ARIMA_Model()


    except Exception as e:
        print(e)








if __name__ == '__main__':
    main()