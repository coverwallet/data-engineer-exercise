# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:41:19 2020

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
from flask import Flask, request, render_template, jsonify

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

print('\n')
print('Poner en el navegador "http://localhost:5000/api/v1/weather/<ciudad>" donde ciudad puede ser Madrid, San_Francisco o New_York')
print('Tambien desde una consola python "request.get("http://localhost:5000/api/v1/weather/<ciudad>")", donde ciudad puede ser Madrid, San_Francisco o New_York')
print('Pulsar ctrl+c para cancelar')
print('\n')


if '__file__' in locals():
    wd = os.path.dirname(__file__)
    sys.path.append(wd)
    sep = '/'
else:
    wd = os.path.abspath('./Documents/Repositorio_Iv/data-engineer-exercise/working_folder/app/')
    wd = wd + '/'
    sys.path.append(wd)
    sep = '/'

### Conexion a la bbdd 
# 
user = 'ivan_1'
password = 'mantga43'
dabase_name = 'weather_db'
client = pymongo.MongoClient("mongodb+srv://%s:%s@cluster0.vsp3s.mongodb.net/%s?retryWrites=true&w=majority" %(user, password, dabase_name))
db = client.get_database(dabase_name)
## Creacion de la app
#
app = Flask(__name__) 

@app.route('/api/v1/weather/<city>', methods=['GET'])
def api_weather_city(city):
    records = 'db.' + city + '_records'
    records = eval(records)
    results = list(records.find({}, {"_id": 0})) # Asi omitimos el _id que por defecto nos agrega mongo
    return jsonify(results)
    

###############################################################################################################
#         INFINITY LOOP LISTENING TO PORT 80 (port=int("80")) TO THE OUTSIDE WORLD (host="0.0.0.0") - START   #
###############################################################################################################
if __name__ == '__main__':
    app.run(
	host="0.0.0.0",
        port=int("5000")
    )
###############################################################################################################
#         INFINITY LOOP LISTENING TO PORT 80 (port=int("80")) TO THE OUTSIDE WORLD (host="0.0.0.0") - END     #
###############################################################################################################

## END ##     