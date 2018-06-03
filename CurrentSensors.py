import numpy as np
import pandas as pd
import datetime
import  matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time


df = pd.read_csv('mFiminute5.csv')

#CREATE DATAFRAME
df1 = pd.DataFrame(df,columns=['time', 'size', 'sId', 'max', 'min', 'ave', 'last_val', 'last_val_time'])


#CONVERSION EPOCH TO HUMAN TIME
df1['last_val_time']=df1['last_val_time']/1000
df1['last_val_time'] = df1['last_val_time'].apply(lambda x: datetime.datetime.fromtimestamp(x))
df1['time']=df1['time']/1000
df1['time'] = df1['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))

#IDENTIFICAR SENSOR 1 o 2
df1['sId'] = df1['sId'].apply(lambda  x: 'Sensor1' if x == 'ObjectId(59de90453004f138372d638f)' else 'Sensor2')


maximo=df1['max'].max()
minimo=df1['min'].min()
media=df1['last_val'].mean()


s1= df1[df1['sId'] == 'Sensor1']
s2= df1[df1['sId'] == 'Sensor2']


#GRAFICAR SENSORES
fig, ax = plt.subplots()
fig.autofmt_xdate()                     #Para adaptar indice x a formato fecha

plt.xlabel('Fecha y hora')
plt.ylabel('Corriente [amps]')
plt.title('Sensores corriente')
plt.plot(s1['time'], s1['ave'])
plt.plot(s2['time'], s2['ave'])

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))   #to get a tick every 3 hours
ax.xaxis.set_major_formatter(xfmt)

plt.plot(s1['time'][s1['ave']> 15], s1['ave'][s1['ave'] > 15], 'ro') #Marcar con un circulo (ro= red o) los puntos por encima de 40
plt.plot(s1['time'][s1['ave']<0.007], s1['ave'][s1['ave'] < 0.007], 'ro') #Marcar con un ciruclo (ro) los puntos por encima de 40
plt.plot(s2['time'][s2['ave']> 15], s2['ave'][s2['ave'] > 15], 'bo') #Marcar con un circulo (bo) los puntos por encima de 40
plt.plot(s2['time'][s2['ave']< 0.007], s2['ave'][s2['ave'] < 0.007], 'bo') #Marcar con un circulo (bo) los puntos por encima de 40



plt.close()