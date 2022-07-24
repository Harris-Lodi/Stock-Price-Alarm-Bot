# Stock-Price-Alarm-Bot

Based on tutorial by Neuralnine:
https://www.youtube.com/watch?v=qkphpFhkHTs

Requirements:

 - pandas-datareader
 - winotify (windows only)
 - notify (all OS)

Resources:

Audio Credit:
Music by AlexGrohl from Pixabay
https://pixabay.com/music/rock-stomping-rock-four-shots-111444/

Icon Credit:
<a href="https://www.flaticon.com/free-icons/stocks" title="stocks icons">Stocks icons created by andinur - Flaticon</a>

Notify: https://pypi.org/project/notify-py/

Notify is very limited in functionality but is enoguh for now
Sadly the more complete notification modules are all OS/Desktop 
specific, ie Windows only or Mac only or Gnome/KDE only

Will need to create a custom notification box module later with
either TKinter or imgui for python, or just imgui for C++ extended
for python for a custom cross platform solution

Actually notify works in a limited fashion, use only 2 second audio clips, nothing longer

Defintely need to make a custom notification system/GUI later!

********************************************************

Stock scraper:

Reference: https://www.youtube.com/watch?v=7sFCOunKL_Y

Requirments:

 - pip install beautifulsoup4
 - pip install requests
 - pip install selenium

Need to now write function to convert json to SQL

For the financial data, found a second site to scrape from, this new site is probably better then Yahoo Financials as it has more data and is easier to work with:
https://stockanalysis.com/stocks/amd/

Reddit Scraping tutorial:
https://www.geeksforgeeks.org/scraping-reddit-using-python/

The financial data was only for annual income, there is about 7 other pages in the financial tab alone to scrape and will thus need a new class for each one
Selenium is recommended as a better way to scrape dynamic table data, but for now this will do!