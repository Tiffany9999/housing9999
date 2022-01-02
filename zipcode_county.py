# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:45:19 2021

@author: Elaine
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import os
path_0 = os.getcwd()


def to_county(zip_code):   
    # open the webpage
    path = 'https://www.getzips.com/cgi-bin/ziplook.exe?What=1&Zip={}&Submit=Look+It+Up'.format(zip_code)
    html = urlopen(path)
    
    bs = BeautifulSoup(html.read(), 'lxml')
    
    
    # roll within the webpage
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(path_0 + '/chromedriver', options = options)
    driver.get(path)
    
    
    
    bs = BeautifulSoup(driver.page_source, 'lxml')
    table = bs.findAll('table')
    
    td = table[-1].findAll('td')
    county = td[6].text
    
    return county
