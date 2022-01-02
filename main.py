#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:10:10 2021

@author: marcus
"""

import backend
import frontend
import school
import house
import numpy as np
import pandas as pd
from pmdarima.arima import auto_arima
import os
import re
import math
import random
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import tkinter as tk  
import tkinter.messagebox
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from PIL import ImageTk

def main():
    print("--------Welcome to Quadruple Z--------")
    print("Please enter 0 if you would like to use the data from our offline database,")
    print("or enter 1 if you would like to do live scraping.")
    print("(Enter anything else to quit)")
    is_livescraping = input()
    if (is_livescraping != '1') & (is_livescraping != '0'):
        return
    if is_livescraping == '0':
        print("Please only enter one of the following zip codes included from our database:")
        print("'15213', '15232', '15217', '15219', '15222', '19104', '19103', '19122', '19134', '19148'")
        print("Otherwise, you will be automatically transfered to live scraping:")
        print("You can now enter:")
        zip_code = input()
        zip_codes = ['15213', '15232', '15217', '15219', '15222', '19104', '19103', '19122', '19134', '19148']
        if zip_code in zip_codes:
            res = backend.recall(zip_code, False)
        else:
            if re.search(r'^[0-9][0-9][0-9][0-9][0-9]$', zip_code) != None:
                res = backend.recall(zip_code, True)
            else:
                print("Query invalid, Please run the program again!")
    else:
        print("Note that web scraping may take 2 minutes.")
        print("Please enter 5-digit zip code below:")
        zip_code = input()
        if re.search(r'^[0-9][0-9][0-9][0-9][0-9]$', zip_code) != None:
            res = backend.recall(zip_code, True)
        else:
            print("Query invalid, Please run the program again!")
            return
    print(res['summary'])
    return res['summary']

if __name__ == '__main__':
    frontend.frontend("")
    res = main()
    frontend.frontend(res)
        
    