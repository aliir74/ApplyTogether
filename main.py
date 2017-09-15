from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver
import time
import csv

url = 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2017/architecture'
url2 = 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2017/computer-science-information-systems'

browser = webdriver.Chrome("/home/ali/Software/chromedriver")
browser.set_window_size(1366, 638)
browser.set_page_load_timeout(120)

def getUrlUniversities(url, field) :
    global browser
    browser.get(url)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    unis = soup.find_all('tbody')[0].find_all('tr')
    list = []
    for i in unis:
        rank = i.findChildren('span', {'class': 'rank'})[0].text
        if(rank[0] == '='):
            rank = rank[1:]
        name = i.findChildren('td', {'class': 'uni'})[0].findChildren('a', {})[0].text
        country = i.findChildren('td', {'class': 'country'})[0].findChildren('img')[0].get('alt')
        d = {'name': name, 'country': country, field: rank}
        list.append(d)
    return list

def merge(l1, l2, f1, f2):
    ans = l1[:]
    for i in l2:
        b = False
        for j in range(len(l1)):
            if(i['name'] == ans[j]['name']):
                ans[j][f2] = i[f2]
                b = True
                break
        if(not b):
            ans.append(i)
    return ans

def writeToCSV(d, f1, f2):
    f = open('Final.csv', 'wt')
    writer = csv.writer(f)
    writer.writerow(['University', 'Country', f1.capitalize(), f2.capitalize()])
    for i in d:
        l = [i['name'], i['country']]
        if(f1 in i) :
            l.append(i[f1])
        if(f2 in i):
            l.append(i[f2])
        writer.writerow(l)
    f.close()


arch = getUrlUniversities(url, 'arch')
comp = getUrlUniversities(url2, 'cs')
result = merge(arch, comp, 'arch', 'cs')
writeToCSV(result, 'arch', 'cs')

browser.quit()