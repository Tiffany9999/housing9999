# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:45:19 2021

@author: Marcus
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import re
path = os.getcwd()

def gosearch(search_key, file_name, write_kind):

    # Initialize Selenium
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(path + '/chromedriver', options = options)
    # Open trulia
    driver.get("https://www.trulia.com/PA/Pittsburgh/15232/")
    
    
    

    search = driver.find_element_by_id("locationInputs")
    search.click()
    search = driver.find_element_by_id("locationInputs")
    search.send_keys(Keys.CONTROL+'a')
    search.send_keys(search_key + "\n")
    sleep(5)
    housecard = driver.find_elements_by_xpath("//div[@data-testid='property-card-details']")
    
    raw = open(path + '/test_raw.txt','w', encoding = 'utf-8')
    
    
    for house in housecard:
        if re.search(r''+(search_key + '$'), house.text) != None:
            raw.write(search_key + '\n' + house.text + '\n')

    try:
        nextpage = driver.find_element_by_xpath("//a[@aria-label='Next Page']")
        flag = True
    except:
        flag = False
        
    while (flag):
        try:
            nextpage.click()
        except Exception:
            break;
        sleep(5)
        housecard = driver.find_elements_by_xpath("//div[@data-testid='property-card-details']")
        for house in housecard:
            if re.search(r''+(search_key + '$'), house.text) != None:
                raw.write(search_key + '\n' + house.text + '\n')
    
    raw.close()
    raw = open(path + '/test_raw.txt','r')
    res = open(path + '/' + file_name, write_kind, encoding = 'utf-8')
    if not os.path.getsize(file_name):
        res.write("Zip Code,House Price,# Bedrooms,# Bathrooms,Area in sqft,Address 1,City,State\n")
    flag = 1
    for line in raw:
        if re.search(r'^[0-9][0-9][0-9][0-9][0-9]$', line) != None:
            flag = 1
        if flag == 1:
            res.write(line[:-1] + ',')
            flag += 1
            continue
        if flag == 2:
            if re.search(r'^\$', line) != None:
                res.write(re.sub('[\$\+\,\\n]', '', line) + ",")
                flag += 1
                continue
            else:
                res.write(',')
                flag += 1
        if flag == 3:
            if re.search(r'bd$', line) != None:
                res.write(line[:-3] + ',')
                flag += 1
                continue
            else:
                res.write(',')
                flag += 1
        if flag == 4:
            if re.search(r'ba$', line) != None:
                res.write(line[:-3] + ',')
                flag += 1
                continue
            else:
                res.write(',')
                flag += 1
        if flag == 5:
            if re.search(r'sqft$', line) != None:
                res.write(re.sub("\,","",line[:-6]) + ",")
                flag += 1
                continue
            else:
                res.write(',')
                flag += 1
        if flag == 6:
            if re.search(r',$', line) != None:
                res.write(re.sub("\\n","",line))
                flag += 1
                continue
            else:
                continue
        if flag == 7:
            res.write(line.replace(' ', '')[:-6] + '\n')
            flag = 1
    raw.close()
    res.close()
    driver.close()

if __name__ == '__main__':
    # # Initialize Selenium
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(path + '/chromedriver', options = options)
    # # Open trulia
    # driver.get("https://www.trulia.com/PA/Pittsburgh/15232/")
    zip_codes = ["15213", "15232", "15217", "15219", "15222", "19104", "19103", "19122", "19134", "19148"]
    #gosearch("15201", 'houses.csv', 'w')
    
    for i in range(len(zip_codes)):
        if i == 0:
            gosearch(zip_codes[i], 'houses_demo.csv', 'w')
        else:
            gosearch(zip_codes[i], 'houses_demo.csv', 'a')
    

