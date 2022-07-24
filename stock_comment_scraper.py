import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd 

# for stockanalysis.com use selenium
# for yahoo finace, this is not enough since the comments page shows limited comments, but might be enough actually for minute level tickers

comments = []
times = []
names = []

header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}

stock = 'AMD'

url = 'https://finance.yahoo.com/quote/'+ stock +'/community?p=' + stock
r = requests.get(url, headers = header)
data = BeautifulSoup(r.text, 'html.parser')

# print(data.text)

comments_list = data.find('div', {'class': 'comments-body'})
comments_data = comments_list.find('ul').find_all('li')

for comment in comments_data:
    comments_text = comment.find('div', {'class': 'Wow(bw)'}).text
    comments_header = comment.find('div', {'class': 'Fz(12px) Mend(20px) Mb(5px)'})
    comments_time = comments_header.find('span', {'class': 'Fz(12px) C(varBattleship)'})
    print(comments_time)
    comments.append(comments_text)
    names.append(comments_header.text)
    times.append(comments_time)

# print(comments_data[1])
# print(comments[1])
# print(times[1])
# print(names[1])

# for some reason the time of the comments does not get scraped, but this can be resolved by pandas dataframe to orgnanize them, will have to keep track of comments
# and compared them to prevent duplicates