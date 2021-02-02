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
import pandas as pd
import requests as rq
import json
import datetime
#import numpy as np
#import csv
#import time
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

def lectura_api_2(fecha_inicio = '2020/12/01', fecha_fin = '2020/12/05'):
    '''
    Este script obtiene de la api las previsiones para los días comprendidos 
    entre fecha inicio y fecha fin
    para las localizaciones 'Madrid', 'San Francisco', 'New York'
    
    Si en la ejecucion desde el cmd no se le indica ninguna fecha de inicio o 
    fin, toma por defecto 5 días entre el 1 y el 5 de diciembre de 2020 
    
    La ejecucion seria "python lectura_api_2.py fecha_inicio fecha_fin"
    Donde fecha_inicio y fecha_fin tienen que tener el formato yyyy/mm/dd
    '''
    
    ## Formamos la lista de fechas ###
    #
    fec_ini = datetime.datetime.strptime(fecha_inicio, '%Y/%m/%d')
    fec_fin = datetime.datetime.strptime(fecha_fin, '%Y/%m/%d')
    dif_days = abs((fec_fin - fec_ini).days)
    lista_fechas = []

    for i in range(dif_days+1):
        lista_fechas.append(fec_ini + datetime.timedelta(days=i))
        
    lista_fechas = [x.strftime('%Y/%m/%d') for x in lista_fechas]
    
    ### Conexion API ###
    #
    """
    Vamos a localizar el id para 3 ciudades: Madrid, San Francisco y New York
    """
    url = 'https://www.metaweather.com'
    header = {'Content-Type':'application/json'}
    ciudades = ['Madrid', 'San Francisco', 'New York']
    
    for item in ciudades:
        df_tot = pd.DataFrame()
        peticion_1 = rq.get(url + f'/api/location/search/?query={item}', header)
        id = json.loads(peticion_1.content.decode("utf-8"))[0]["woeid"]
        for item2 in lista_fechas:
            peticion_2 = rq.get(url + f'/api/location/{id}/{item2}', header)
            consolidated_weather = json.loads(peticion_2.content.decode("utf-8"))
            df = pd.DataFrame(consolidated_weather)
            df_tot = pd.concat([df_tot, df])
        item_str = item.replace(' ', '_')
        df_tot.to_csv(wd + f'consolidated_weather_{item_str}.csv', index=False)
    print(f'Lectura correcta, los .csv están en el working_folder: {wd}')
    return


if __name__ == '__main__':
    try:
        fecha_inicio = sys.argv[1]
        fecha_fin = sys.argv[2]
    except:
        fecha_inicio = []
        fecha_fin = []
        pass
    if ((fecha_inicio == []) | (fecha_fin == [])):
        lectura_api_2()
    else:
        lectura_api_2(fecha_inicio, fecha_fin)

## END ##