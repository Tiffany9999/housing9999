#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:03:46 2021

@author: marcus,wendy,kelly,yz
"""
import house
import school
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from pmdarima.arima import auto_arima
import os
import re
import math
import random
path = os.getcwd()


online_scrap = False
search_query = '15232'

def recall(search_query, online_scrap):
    res = {}
    zip_codes = ['15213', '15232', '15217', '15219', '15222', '19104', '19103', '19122', '19134', '19148']
    
    if (online_scrap == True) | (search_query not in zip_codes):
        try:
            # 此处调用三个爬虫函数
            house.gosearch(search_query, 'houses.csv', 'w')
            school.school_search(search_query)
        except Exception:
            print('Sorry, no data found!')
            res['info'] = 'Sorry, an error occured when scraping the data!'
            return res
    if online_scrap == True:
        schools = pd.read_csv(path + '/schools.csv')
    else:
        schools = pd.read_csv(path + '/schools_demo.csv')
    schools = schools[schools['Zip Code'] == int(search_query)].reset_index()
    if online_scrap == True:
        houses = pd.read_csv(path + '/houses.csv')
    else:
        houses = pd.read_csv(path + '/houses_demo.csv')
    houses = houses[houses['Zip Code'] == int(search_query)].reset_index()
    races = pd.read_csv(path + '/races.csv')
    if online_scrap == True:
        races = races[races['Zip Code'] == random.randint(10000, 10064)].reset_index()
    else:
        races = races[races['Zip Code'] == int(search_query)].reset_index()
    price_ts = pd.read_csv(path + "/price time series.csv")
    price_ts = price_ts.loc[price_ts['Zip Code'] == int(search_query)].reset_index()
    if len(price_ts) == 0:
        price_ts = pd.read_csv(path + "/price time series.csv")
        price_ts = price_ts.loc[price_ts['Zip Code'] == 77777].reset_index()
    
    res['info'] = 'Search completed!'
    
    # Analyzing School Data
    if (len(schools) == 0):
        res['schoolinfo'] = 'No school found in this area.'
        school_score = 0.0
    else:
        n = len(schools)
        schools['Score'] = [0.0] * n
        # Calculate school score
        for i in range(0, n):
            proficiency = (float(schools['Math Proficiency'][i]) + float(schools['Reading Proficiency'][i])) / 2
            distance = 100.0 - (float(schools['Distance'][i]) / 5.0 * 100)
            schools['Score'][i] = proficiency * 0.8 + distance * 0.2
        # Calculate overall score
        school_score = schools['Score'].mean()
        # Sort by score
        schools.sort_values(by = ['Score'], ascending = False, na_position='last', inplace = True)
        schools.to_csv(path + '/result_school.csv', index = None)
        res['schoolinfo'] = 'Found ' + str(n) + ' school results, sorted by SCORE:'
        # if n <= 10:
        #     res['school'] = schools.to_string() + '\nRefer to result_school.csv for full result.'
        # else:
        #     res['school'] = schools.iloc[[0, 10], :].to_string() + '\n......\nand' + str(n-10) + 'more results.' + '\nRefer to result_school.csv for full result.'
    
    # Analyzing House Data
    if (len(houses) == 0):
        res['houseinfo'] = 'No house found in this area.'
        houses_score = 0.0
    else:
        n = len(houses)
        houses['Score'] = [0.0] * n
        # Calculate house score
        for i in range(0, n):
            if math.isnan(houses['# Bedrooms'][i]) | math.isnan(houses['# Bathrooms'][i]) | math.isnan(houses['Area in sqft'][i]):
                houses['Score'][i] = 0.0
            else:
                price_index = 10000.0 / (float(houses['House Price'][i]) / float(houses['Area in sqft'][i]))
                room_index = (float(houses['# Bedrooms'][i]) + float(houses['# Bathrooms'][i])) / 10
                houses['Score'][i] = min(100.0, price_index + (100 - price_index) * room_index)
        # Calculate overall score
        houses_score = houses['Score'].mean()
        # Sort by score
        houses.sort_values(by = ['Score'], ascending = False, na_position='last', inplace = True)
        houses.to_csv(path + '/result_house.csv', index = None)
        res['houseinfo'] = 'Found ' + str(n) + ' house results, sorted by SCORE:'
        # if n <= 10:
        #     res['house'] = schools.to_string() + '\nRefer to result_house.csv for full result.'
        # else:
        #     res['house'] = schools.iloc[[0, 10], :].to_string() + '\n......\nand' + str(n-10) + 'more results.' + '\nRefer to result_house.csv for full result.'
    
    # Analyzing Race Data
    if (len(races) == 0):
        res['raceinfo'] = 'No race information found in this area.'
        race_score = 50
    else:
        res['raceinfo'] = 'Race distribution can be concluded below:\n'
        # Generate race distribution pie chart
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.figure(figsize=(7.5,5),dpi=80) 
        labels = races.columns.values.tolist()[3:]
        sizes = races.values.tolist()[0][3:]
        colors = ['red','yellowgreen','lightskyblue','yellow','purple','pink','peachpuff','orange'] 
        explode = [0.01] * (races.shape[1] - 2)
        plt.figure(figsize=(18,7))
        patches,text1,text2 = plt.pie(sizes,
                      #explode=explode,
                      labels=labels,
                      colors=colors,
                      radius=10,
                      labeldistance = 1.2,
                      autopct = '%d%%', 
                      shadow = False, 
                      startangle =90, 
                      pctdistance = 0.6) 
        plt.axis('equal')
        plt.legend(loc = 4)
        plt.title("Race Distribution in" + search_query)
        plt.savefig('./race_result.jpg')
        res['race'] = 'race_result.jpg'
        plt.show()
        # Calculate overall race score
        race_mean = np.mean(sizes)
        race_std = np.std(sizes, ddof = 1)
        race_score = max(0.0, (1 - race_std / race_mean) * 100)

    # Analyzing House Prize Time Series
    months = price_ts.columns.values.tolist()[6:]
    price_ts = price_ts.iloc[:, 6:].T
    price_ts.columns = ['price']
    price_ts['month'] = months
    price_ts['month'] = pd.to_datetime(price_ts['month'])
    price_ts.set_index('month', inplace=True)
    model = auto_arima(price_ts, trace = True, error_action = 'ignore', suppress_warnings = True)
    model.fit(price_ts)
    forecast = model.predict(n_periods = 6)
    forecast = pd.DataFrame(forecast, columns = ['price'])
    forecast['month'] = ['2021-09-30', '2021-10-30', '2021-11-30', '2021-12-31', '2022-01-31', '2022-02-28']
    forecast['month'] = pd.to_datetime(forecast['month'])
    forecast.set_index('month', inplace=True)
    fig = plt.figure()
    fig.add_subplot()
    #fig.set_title(search_query + 'house price forecast for the next 6 months')
    plt.plot(price_ts, 'b-', label = 'Real Data')
    plt.plot(forecast, 'r-', label = 'Forecast Data')
    plt.legend(loc = 'best')
    plt.title(search_query + ' house price forecast for the next 6 months')
    plt.savefig('./time_series.jpg')
    plt.show(block = False)
    res['tsplot'] = 'time_series.jpg'
    res['ts_summary'] = 'Forcast average price for the next 6 months: \n'\
                        + str(forecast.iloc[0, 0])[0:9] + ' ' \
                        + str(forecast.iloc[1, 0])[0:9] + ' ' \
                        + str(forecast.iloc[2, 0])[0:9] + ' ' \
                        + str(forecast.iloc[3, 0])[0:9] + ' ' \
                        + str(forecast.iloc[4, 0])[0:9] + ' ' \
                        + str(forecast.iloc[5, 0])[0:9] \
                        + '\nThe estimated annualized rate of return is '\
                        + str((pow((forecast.iloc[5, 0] / forecast.iloc[0, 0]), 2) - 1) * 100)[0:5] + '%'
    
    # Generalize summary string
    summary = ''
    summary += 'Search completed!\n\n'
    summary += res['schoolinfo'] + '\n\n'
    summary += res['houseinfo'] + '\n\n'
    summary += 'Race distribution can be found in the race page\n\n'
    summary += res['ts_summary'] + '\n\n'
    summary += 'The school quality score of ' + search_query + ' is ' + str(format(school_score, '.2f')) + ' out of 100\n'
    summary += 'The house quality score of ' + search_query + ' is ' + str(format(houses_score, '.2f')) + ' out of 100\n\n'
    if (school_score < 60.0) | (houses_score < 60.0) | ((forecast.iloc[5, 0] / forecast.iloc[0, 0]) < 1.0):
        summary += 'In summary, it is not a good place for your children to study, as well as for you to live!'
    else :
        summary += 'In summary, it is an ideal place for your children to study, as well as for you to live!'
    res['summary'] = summary

    return res
    
if __name__ == '__main__':
    #res = recall('15206', True)
    #print(res.get('info'))
    # print(res['schoolinfo'])
    # print(res['houseinfo'])
    # print(res['raceinfo'])
    # print(res['race'])
    # print(res['tsplot'])
    # print(res['ts_summary'])
    print(res['summary'])
