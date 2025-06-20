import logic
import API
import Storing

def main():
    try:
        symbol  = input('Please input the company stock you\'d like to check:\n')
        API.get_get_stock(symbol)
    except Exception as e:
        print(e)








if __name__ == '__main__':
    main()