import requests
from bs4 import BeautifulSoup
import time
import json

headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}

tickers = ['SPY', 'AMD', 'AAPL', 'NVDA', 'TSLA', 'INTC', 'NFLX']
stockData = []

# the following 3 were found by inspecting the code for the price 
data_type = 'div'
data_class = 'D(ib) Mend(20px)'
sub_class_data_type = 'fin-streamer'

def getData(symbol):

    url = 'https://finance.yahoo.com/quote/' + symbol +'?p=' + symbol + '&.tsrc=fin-srch'

    r = requests.get(url)

    # if r.status_code is 200, then you are good!
    # print(r.status_code)
    # bring back text from page
    # print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')

    # test soup
    # print(soup.title.text)

    # The following has an issue when using different tickers, not all tickers use the same fin-streamer class names

    '''

    # high light the closing price in sight, inspect element, type is before class 'fin-streamer' and class is next to it!
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    price_change = soup.find('fin-streamer', {'class': "Fw(500) Pstart(8px) Fz(24px)"})

    #price_data_field = price.find('fin-streamer', {class_': "value"})

    # find closing price from specific inspected item's class
    print(price)
    #print(price_data_field)
    # print(price_change)

    '''
    # price_main was found by highlighting the price bar, and finding the root common div
    price_main = soup.find(data_type, {'class': data_class}).find_all(sub_class_data_type)
    price = price_main[0].text
    price_change_value = price_main[1].text 
    price_change_percent = price_main[2].text 

    # create a dictionary that will be returned from this function that contains the scraped data
    stock = {
        'symbol': symbol,
        'price': price,
        'value-change': price_change_value,
        'percent-change': price_change_percent
    }

    return stock

    # print(price, price_change_value, price_change_percent)
    # print("The price and it's changes for " + symbol + " are: " + price + ", " + price_change_value + ", " + price_change_percent)


# add all dictionary data to a list
for ticker in tickers:
    stockData.append(getData(ticker))
    time.sleep(5)
    print('Getting, ', ticker)

# print(stockData)

# convert list to json file
with open('stockData.json', 'w') as f:
    json.dump(stockData, f)

print('PRocess Finished')