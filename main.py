from bs4 import BeautifulSoup
import csv
import requests


url = 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2017/architecture'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find(id='qs-rankings')
print(table)