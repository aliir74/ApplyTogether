from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver



url = 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2017/architecture'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find(id='qs-rankings')
print(soup.prettify())

browser = webdriver.Chrome("/home/ali/Software/chromedriver")
browser.set_window_size(1366, 638)
browser.set_page_load_timeout(120)