#!/usr/bin/python
import re
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

bat_soup = soup.find_all("div", {"id": "maincounter-wrap"})

# print(bat_soup)
# print(bat_soup.prettify())

titles =[]
for block in bat_soup:
    # titles.append(get.text(block))
    titles.append(block.find("h1").get_text())

counts=[]
for block in bat_soup:
    counts.append(block.find("span").get_text())

# print(counts)
# [<div id="maincounter-wrap" style="margin-top:15px"> <h1>Coronavirus Cases:</h1> <div class="maincounter-number"> <span style="color:#aaa">145,638 </span> </div></div>, <div id="maincounter-wrap" style="margin-top:15px"> <h1>Deaths:</h1> <div class="maincounter-number"> <span>5,436</span> </div></div>, <div id="maincounter-wrap" style="margin-top:15px;"> <h1>Recovered:</h1> <div class="maincounter-number" style="color:#8ACA2B "> <span>72,529</span> </div></div>]
cases_count=re.sub('\D','',counts[0])
death_count=re.sub('\D','',counts[1])

print(cases_count, death_count)
