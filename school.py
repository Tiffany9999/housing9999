# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:45:19 2021

@author: Elaine
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
path_0 = os.getcwd()


# scrap the contents from the webpage
def scrap_string(category, class_name, index, bs):
    contents = []
    table_list = bs.findAll(category, {"class": class_name})
    for i in table_list:
        j = list(i.strings)
        contents.append(j[index])
    
    return contents



# text Type contents
def scrap_text(category, class_name, index, bs):
    contents = []
    table_list = bs.findAll(category, {"class": class_name})
    for i in table_list[1:]:
        j = i.text
        
        grade = j.split(' ')
        j = ''.join(grade[index])
        
        # for distance
        if j == '-':
            j = 0
        
        
        contents.append(j)
    
    return contents

# location
def scrap_location(category, class_name, bs):
    contents = []
    table_list = bs.findAll(category, {"class": class_name})
    for i in table_list[1:]:
        j = list(i.strings)
        j = ' '.join(j[0:2])
        contents.append(str(j))
    
    return contents

# telephone
def scrap_telephone(category, class_name, index, bs):
    contents = []
    table_list = bs.findAll(category, {"class": class_name})
    for i in table_list[1:]:
        j = list(i.strings)
        contents.append(j[index])
    
    return contents



# inner link
def scrap_link(category,class_name, bs):
    contents = []
    table_list = bs.findAll(category, {"class": class_name})
    for i in table_list:
        item = i.select('div a')[0]
        link = "https://www.publicschoolreview.com/" + item.get('href')
        contents.append(link)
    
    return contents

# get proficiency
def scrap_proficiency(category, class_name, index, bs):
    contents = []
    table_list = bs.findAll(category, {"class": class_name})
    for i in table_list:
        j = list(i.strings)
        
        if len(j) < 4:
            contents.append("to be added")
        else:
            for m in j:
                if "Math" in m:
                    contents.append(m)

    return contents


# calculate proficiency
def proficiency_score(proficiency):
    math_score = []
    reading_score = []
    for i in proficiency:
        if i == "to be added":
            math_score.append(0)
            reading_score.append(0)
        else:
            number = re.findall(r'[0-9]+', i)
    
            # calculate math & reading
            if len(number) == 4:
                math = (int(number[0])+int(number[1]))/2
                reading = (int(number[2])+int(number[3]))/2
            
            if len(number) == 3 and (int(number[1]) - int(number[0])) < 10:
                math = (int(number[0])+int(number[1]))/2
                reading = int(number[2])
            elif len(number) == 3 and (int(number[1]) - int(number[0])) >= 10:
                math = int(number[0])
                reading = (int(number[1])+int(number[2]))/2
            
            if len(number) == 2:
                math = int(number[0])
                reading = int(number[1])
            
            math_score.append(math)
            reading_score.append(reading)
        
    return math_score, reading_score

# fill missing score
def fill(list_name):
    average = sum(list_name)/(len(list_name)-list_name.count(0))
    for i in range(len(list_name)):
        if list_name[i] == 0:
            list_name[i] = float(format(average, '.1f'))
            
    return list_name


# scrap and continuously add new info
def operations(bs):
    school_name = scrap_string('div', "tpl-school-detail", 0, bs)
    student_number = scrap_text('div', "tp-list-column column5", 2, bs)
    grade = scrap_text('div', "tp-list-column column4", 1, bs)
    proficiency = scrap_proficiency('div', "tpl-school-detail", 0, bs)
    location = scrap_location('div', "tp-list-column column2", bs)
    telephone = scrap_telephone('div', "tp-list-column column2", 2, bs)
    detail = scrap_link('div', "tpl-school-detail", bs)
    distance = scrap_text('div', "tp-list-column column3", 0, bs)
    
    return school_name, student_number, grade, proficiency, location, telephone, detail, distance


# enter function
def school_search(zip_code):
    # open the webpage
    path = 'https://www.publicschoolreview.com/find-schools-by-zipcode/{}/5/none/0'.format(zip_code)
    # path = 'https://www.publicschoolreview.com/find-schools-by-zipcode/15217/5/none/0'
    html = urlopen(path)
    bs = BeautifulSoup(html.read(), 'lxml')
    
    # fout = open('draft.txt', 'wt', encoding = 'utf-8')
    
    # create a csv
    fout = open("schools.csv", 'w', encoding = 'utf-8', newline = "")
    csv_write = csv.writer(fout)
    
    # create and write the head
    csv_write.writerow(["Zip Code", "School", "Math Proficiency", "Reading Proficiency", "Grades", "Location", "Distance", "Students","Telephone", "Details"])
    
    # roll within the webpage
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(path_0 + '/chromedriver', options = options)
    driver.get(path)
    
    while True:
        try:
            driver.find_element_by_id("tpl-showmore").click()
        except Exception:
            break
    
        # operate all the info
        bs = BeautifulSoup(driver.page_source, 'lxml')
    
    
    # one more time
    bs = BeautifulSoup(driver.page_source, 'lxml')
    school_name, student_number, grade, proficiency, location, telephone, detail, distance = operations(bs)
    math, reading = proficiency_score(proficiency)
    math = fill(math)
    reading = fill(reading)
    
    
    # write all the contents into csv
    schools = []
    for i in range(len(school_name)):
        school = []
        school.append(str(zip_code))
        school.append(school_name[i])
        school.append(math[i])
        school.append(reading[i])
        grade[i] = grade[i].replace('-', '~')
        school.append(grade[i])
        school.append(location[i])
        school.append(distance[i])
        school.append(student_number[i])
        school.append(telephone[i])
        school.append(detail[i])
        
        
        schools.append(school)
        
    for i in schools:
        csv_write.writerow(i)
    
    # print(len(school_name))
    
    fout.close()

if __name__ == '__main__':    
    school_search('15213')