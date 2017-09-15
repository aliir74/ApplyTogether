from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver


url = 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2017/architecture'
url2 = 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2017/computer-science-information-systems'

browser = webdriver.Chrome("/home/ali/Software/chromedriver")
browser.set_window_size(1366, 638)
browser.set_page_load_timeout(120)
browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')
table = soup.find(id='qs-ranking')
unis = soup.find_all('tbody')[0].find_all('tr')
list = []
for i in unis:
    rank = i.findChildren('span', {'class': 'rank'})[0].text
    if(rank[0] == '='):
        rank = rank[1:]
    name = i.findChildren('td', {'class': 'uni'})[0].findChildren('a', {})[0].text
    country = i.findChildren('td', {'class': 'country'})[0].findChildren('img')[0].get('alt')
    print(country)
    #d = {'name': name, 'country': country, 'rank': rank}
    #list.append(d)
    #print(d)
browser.quit()