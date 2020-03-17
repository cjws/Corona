#!/usr/bin/python
import re
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

bat_soup = soup.find_all("div", {"id": "maincounter-wrap"})

titles=[]
for block in bat_soup:
    titles.append(block.find("h1").get_text())

counts=[]
for block in bat_soup:
    counts.append(block.find("span").get_text())

cases_count=re.sub('\D','',counts[0])
death_count=re.sub('\D','',counts[1])

print(cases_count, death_count)
