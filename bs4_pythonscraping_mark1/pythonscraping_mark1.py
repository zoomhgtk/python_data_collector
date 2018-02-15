#! /usr/bin/env/python3

import requests, bs4

res1 = requests.get('http://www.pythonscraping.com/pages/warandpeace.html')
res1.raise_for_status()

bsObj1 = bs4.BeautifulSoup(res1.text)

nameList1 = bsObj1.findAll("span", {"class":"green"})

for name in nameList1:
    print (name.get_text())
