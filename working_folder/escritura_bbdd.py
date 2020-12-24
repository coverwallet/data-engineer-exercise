# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:45:36 2020

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
import pandas as pd
import numpy as np
import requests as rq
import csv
import json
import glob
import pymongo
import dns

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
#print(os.path.dirname(os.path.realpath(__file__)))

if '__file__' in locals():
    wd = os.path.dirname(__file__)
    sys.path.append(wd)
    sep = '/'
else:
    wd = os.path.abspath('./Documents/Repositorio_Iv/data-engineer-exercise/working_folder/')
    wd = wd + '/'
    sys.path.append(wd)
    sep = '/'

def escritura_bbdd(): 
    ### Obtenemos lista de ficheros ###
    #
    lista_ficheros = glob.glob(wd + '*.csv')
    
    ### Conexion a la bbdd 
    # 
    user = 'ivan_1'
    password = 'mantga43'
    dabase_name = 'weather_db'
    client = pymongo.MongoClient("mongodb+srv://%s:%s@cluster0.vsp3s.mongodb.net/%s?retryWrites=true&w=majority" %(user, password, dabase_name))
    db = client.get_database(dabase_name)
    
    for item in lista_ficheros:
        item_str = item.split(sep)[-1]
        item_str = item_str.split('.')[0]
        item_str = item_str.split('consolidated_weather_')[-1]
        item_str = item_str + '_records'
        df = pd.read_csv(f'{item}')
        df_json = df.to_json(orient="records")
        df_json = json.loads(df_json)
        exec('records = db.' + item_str)
        exec('records.remove()')
        exec('records.insert(df_json)')
    print('Se han leído los .csv y se han subido como documentos a la base de datos MongoDB Atlas')
    return

if __name__ == '__main__':
    escritura_bbdd()

## END ##