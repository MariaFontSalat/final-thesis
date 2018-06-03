import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import matplotlib.dates as mdates
import random
import math

from tempint import alarmast
from humedad import alarmash
from EnergiaElectrica import alarmase3
from movimiento import alarmasm

from EventsSensors import df1
alarmasc=pd.DataFrame()
alarmasc['event']=df1['rulename']
alarmasc['row']=df1.index
alarmasc['salida']= ''
alarmasc['time']=df1['time']
alarmasc['tiposensor']=df1['sensor']
alarmasc['value']=df1['sensor_value']


TOT=alarmast.append(alarmash, ignore_index=True)
TOT=TOT.append(alarmase3, ignore_index=True)
TOT=TOT.append(alarmasm, ignore_index=True)
TOT=TOT.append(alarmasc, ignore_index=True)
TOT=TOT.sort_values(by='time')


#Importar a excel


writer = pd.ExcelWriter('eventsexport.xlsx')
TOT.to_excel(writer,'Sheet1')
writer.save()

plt.close()

