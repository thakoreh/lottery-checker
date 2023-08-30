from selenium import webdriver
from datetime import timedelta, date
import requests
from bs4 import BeautifulSoup
import re
from time import sleep

ormb = open('or_megabucks.csv','a')
ormb_err = open('or_megabucks_errors.csv','w')
ormb.write(','.join(['drawdate','n1','n2','n3','n4','n5','n6','winners6','winners5','winners4','prize6','prize5','prize4'])+'\n')
start_date = date(2023,8,10)
end_date = date(2023,8,16)
current = start_date

driver = webdriver.Firefox()
driver.get('http://www.oregonlottery.org/games/draw-games/megabucks/past-results')

while current < end_date:
    while current.strftime('%w') not in ['1','3','6']:
        current = current + timedelta(1)    
    driver.find_element_by_id("FromDate").clear()
    driver.find_element_by_id("ToDate").clear()
    driver.find_element_by_id("FromDate").send_keys(current.strftime('%m/%d/%Y'))
    driver.find_element_by_id("ToDate").send_keys(current.strftime('%m/%d/%Y'))
    driver.find_element_by_css_selector(".viewResultsButton").click()
    sleep(30)
    soup = BeautifulSoup(driver.page_source)
    test1 = soup.find_all("td")
    numbers = [test1[i].get_text() for i in range(2,8)] 
    test2 = soup.find_all("strong")
    winners = [test2[1].get_text().replace(',','')]
    prizes = [test2[0].get_text().replace('$','').replace(',','')]
    for i in range(0,2):
        winners.append(test2[4*i+3].get_text().replace(',',''))
        prizes.append(test2[4*i+2].get_text().replace('$','').replace(',','')) 
    testdate = test1[0].get_text().split('/')
    testdate = date(int(testdate[2]),int(testdate[0]),int(testdate[1]))
    if current.strftime('%Y-%m-%d') == testdate.strftime('%Y-%m-%d'):
        ormb.write(','.join([testdate.strftime('%Y-%m-%d')] + numbers + winners + prizes)+'\n')
    else:
        ormb_err.write(current.strftime('%Y-%m-%d') + '\n')
    
    current = current + timedelta(1)

ormb.close()
ormb_err.close()