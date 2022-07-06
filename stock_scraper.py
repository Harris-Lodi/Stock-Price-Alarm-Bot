import requests
from bs4 import BeautifulSoup
import time
import json

headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}

tickers = ['SPY', 'AMD', 'AAPL', 'NVDA', 'TSLA', 'INTC', 'NFLX']
stockData = []

# the following were found by inspecting the code for the price 
data_type_price = 'div'
data_class_price = 'D(ib) Mend(20px)'
sub_class_data_type_price = 'fin-streamer'

data_type_details_a = 'div'
data_class_details_a = 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'
sub_class_details_a = 'tr'
sub_data_type_details_a = 'td'
sub_data_class_details_a = 'Ta(end) Fw(600) Lh(14px)'

data_type_details_b = 'div'
data_class_details_b = 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'
sub_class_details_b = 'tr'
sub_data_type_details_b = 'td'
sub_data_class_details_b = 'Ta(end) Fw(600) Lh(14px)'

def getDataSummary(symbol):

    url_summary = 'https://finance.yahoo.com/quote/' + symbol +'?p=' + symbol + '&.tsrc=fin-srch'

    r_summary = requests.get(url_summary)

    # if r.status_code is 200, then you are good!
    # print(r.status_code)
    # bring back text from page
    # print(r.text)

    summary = BeautifulSoup(r_summary.text, 'html.parser')

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
    price_main = summary.find(data_type_price, {'class': data_class_price}).find_all(sub_class_data_type_price)
    price = price_main[0].text
    price_change_value = price_main[1].text 
    price_change_percent = price_main[2].text 

    # getting the front page data
    details_a = summary.find(data_type_details_a, {'class': data_class_details_a}).find_all(sub_class_details_a)
    details_b = summary.find(data_type_details_b, {'class': data_class_details_b}).find_all(sub_class_details_b)

    # store specific values we need from front page data
    previous_close = details_a[0].find(sub_data_type_details_a, {'class': sub_data_class_details_a}).text
    price_open = details_a[1].find(sub_data_type_details_a, {'class': sub_data_class_details_a}).text
    days_range = details_a[4].find(sub_data_type_details_a, {'class': sub_data_class_details_a}).text
    yr_range = details_a[5].find(sub_data_type_details_a, {'class': sub_data_class_details_a}).text
    volume = details_a[6].find(sub_data_type_details_a, {'class': sub_data_class_details_a}).text
    avg_volume = details_a[7].find(sub_data_type_details_a, {'class': sub_data_class_details_a}).text
    market_cap = details_b[0].find(sub_data_type_details_b, {'class': sub_data_class_details_b}).text
    earnings_date = details_b[4].find(sub_data_type_details_b, {'class': sub_data_class_details_b}).text
    forward_dividends_and_yield = details_b[5].find(sub_data_type_details_b, {'class': sub_data_class_details_b}).text
    annual_target_est = details_b[7].find(sub_data_type_details_b, {'class': sub_data_class_details_b}).text

    # create a dictionary that will be returned from this function that contains the scraped data
    stock = {
        'symbol': symbol,
        'price': price,
        'value-change': price_change_value,
        'percent-change': price_change_percent,
        'previous-close': previous_close,
        'previous-open': price_open,
        'todays-range': days_range,
        'annual-range': yr_range,
        'volume': volume,
        'avg-volume': avg_volume,
        'market-cap': market_cap,
        'earnings-date': earnings_date,
        'forward-dividends-&-yield': forward_dividends_and_yield,
        'annual-target-est': annual_target_est
    }

    return stock



# add all dictionary data to a list
for ticker in tickers:
    stockData.append(getDataSummary(ticker))
    time.sleep(5)
    print('Getting, ', ticker)

# print(stockData)

# convert list to json file
with open('stockData.json', 'w') as f:
    json.dump(stockData, f)

print('Process Finished')


# testing new code:

'''

test = getData('AMD')
print(len(test))
print(test[0].text)
print(test[1].text)
print(test[2].text)
print(test[3].text)
print(test[4].text)
print(test[5].text)
print(test[6].text)
print(test[7].text)
'''