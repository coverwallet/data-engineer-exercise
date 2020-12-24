# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:30:40 2020

@author: iv
"""

###############################
## SELECT PLATFORM: ##########
#############################    
###-- WINDOWS OR LINUX --###
###########################
import sys
if sys.platform == 'win32':
    path = ''
    print ('\n#### Windows System ####')
    system = sys.platform
else:
    path = ''
    print ('\n#### Linux System ####')
    system = sys.platform

print ('#####################################')
print ('#####################################')
print ('\n### Importing Libraries... ###')

import os
import sys
import pandas as pd
import requests as rq
import json
#import numpy as np
#import csv
#import time
#import datetime
#import pylab as pl
#import seaborn as sns
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#import lxml
#import urllib
#import statsmodels
#import sklearn
#import nltk
#import scipy
#import tables
#import json, hmac, hashlib, time, requests, base64
#from requests.auth import AuthBase
#import datetime as dt
#import timeit
#import math
#from scipy import stats
#import base64
#import pyspark
#from pyspark import SparkConf, SparkContext
#from pyspark.sql import SparkSession

if '__file__' in locals():
    wd = os.path.dirname(__file__)
    sys.path.append(wd)
else:
    wd = os.path.abspath("./Documents/Repositorio_Iv/data-engineer-exercise/working_folder/")
    wd = wd + '/'
    sys.path.append(wd)


def lectura_api():
    '''
    La ejecucion seria "python lectura_api.py"
    Este primer script lee datos de previsión a 5 días de la api para las 
    localizaciones 'Madrid', 'San Francisco', 'New York' y escribe 
    los .csv correspondientes en la carpeta "working_folder"
    '''

    ### Conexion API ###
    #
    """
    Vamos a localizar el id para 3 ciudades: Madrid, San Francisco y New York
    """
    url = 'https://www.metaweather.com'
    header = {'Content-Type':'application/json'}
    ciudades = ['Madrid', 'San Francisco', 'New York']
    
    for item in ciudades:
        peticion_1 = rq.get(url + f'/api/location/search/?query={item}', header)
        id = json.loads(peticion_1.content.decode("utf-8"))[0]["woeid"]
        peticion_2 = rq.get(url + f'/api/location/{id}', header)
        consolidated_weather = json.loads(peticion_2.content.decode("utf-8"))\
        ['consolidated_weather']
        df = pd.DataFrame(consolidated_weather)
        item_str = item.replace(' ', '_')
        
        df.to_csv(f'{wd}consolidated_weather_{item_str}.csv', index=False)
    print(f'Lectura correcta, los .csv están en el working_folder: {wd}')
    return


if __name__ == '__main__':
    lectura_api()

## END ##