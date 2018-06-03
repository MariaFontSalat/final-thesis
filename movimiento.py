import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import matplotlib.dates as mdates
import math
import openpyxl
from pandas import ExcelWriter

doc4=pd.read_csv('Motion&Door.csv')
df5=pd.DataFrame(doc4,columns=['row','last_val_time','sensor','event'])
df5.rename(columns={'last_val_time':'time'}, inplace=True)

#EPOCH TO HUMAN
df5['time']=df5['time']/1000
df5['time'] = df5['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))

#COMPLETAR CAMPOS VACIOS (con False ya que la probabilidad de False respecto True es mas alta)
df5['event']=df5['event'].fillna(False)

#Identificar sensor
df5['sensor'] = df5['sensor'].apply(lambda  x: 'Sensor movimiento' if x == 1 else 'Sensor puerta')

move=df5[df5['sensor'] == 'Sensor movimiento']
door=df5[df5['sensor'] == 'Sensor puerta']

#Recuento de true's que se han dado (ha ocurrido el evento)
eventmove=np.sum(move['event'])
eventdoor=np.sum(door['event'])

#Dividimos ventana para tener dos graficos
plt.subplot(1,2,1)
plt.pie([eventmove, len(move)-eventmove], labels = ['si','no'])
plt.title(u'% de veces que se detecto movimiento')

plt.subplot(1,2,2)
plt.pie([eventdoor, len(door)-eventdoor], labels=['si','no'])
plt.title(u'% de veces que se abrio la puerta')





#CREAR ALARMA
#DataFrame de la alarma 1
alarmasm=df5[df5['event'] == True]
alarmasm['tiposensor']= df5['sensor']
alarmasm['event']= np.where(alarmasm['tiposensor'] == 'Sensor movimiento', 'Hay movimiento', 'Abre puerta')
alarmasm['value']= df5['event']
del alarmasm['sensor']
#alarmasm['time']=pd.to_datetime(alarmasm['time'])
#alarmasm['nivel']=np.where(datetime.time(hour=9, minute=00, second=00) < alarmasm['time'] < datetime.time(hour=18, minute=00, second=00), alarmasm['nivel'] == 1)

#Ordenamos las alarmas por tiempo
alarmasm=alarmasm.sort_values(by='time')


#print alarmasm['time']
plt.close()




