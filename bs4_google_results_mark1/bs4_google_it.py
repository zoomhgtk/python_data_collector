#! /usr/bin/env/python3

import requests, sys, webbrowser, bs4

print ('Googling...')

res1 = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]), verify=False)
#res1.raise_for_status()

print ('making soup1')

soup1 = bs4.BeautifulSoup(res1.text)

print(type(soup1))

linkElems = soup1.select('.r a')
numOpen = min(5, len(linkElems))
for i in range (numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
