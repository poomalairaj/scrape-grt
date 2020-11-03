import requests
import re
import sys
import csv
import time
import os

os.environ['TZ'] = 'Asia/Kolkata'
time.tzset()

import datetime
from bs4 import BeautifulSoup
from decimal import Decimal

url = 'https://grtjewels.com/'
csv_file = 'grt.csv'

for i in range(5):
    try:
        print("Trying %s for loop %d" % (url, i))
        web_text = requests.get(url).text
    except requests.exceptions.ConnectionError:
        print("Internet connection Error!")
        sys.exit()

    except requests.exceptions.Timeout:
        continue
    else:
        break

soup = BeautifulSoup(web_text, 'html.parser')
gold_price_text = soup.findAll('span', {'class': 'hoverImg'})[0].text
gold_price = re.findall('Rs.\s+(.*)', gold_price_text)
price = Decimal(re.sub(r'[^\d.]', '', gold_price[0]))
print("Gold price is %d" % price)

d = datetime.datetime.now()
current_date = d.strftime('%Y-%m-%d %H:%M:%S')

with open(csv_file, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([current_date, price])

