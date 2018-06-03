import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import matplotlib.dates as mdates
import random
import math

doc1=pd.read_csv('Temperatura int.csv')
df1=pd.DataFrame(doc1,columns=['row','last_val_time','ave'])
df1.rename(columns={'last_val_time':'time','ave':'value'}, inplace=True)

#EPOCH TO HUMAN
df1['time']=df1['time']/1000
df1['time'] = df1['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))

#COMPLETAR CAMPOS VACIOS (con el valor anterior)
df1['value']=df1['value'].fillna(method='ffill')


#GRAFICAR SENSORES
fig, ax = plt.subplots()
fig.autofmt_xdate()                     #Para adaptar indice x a formato fecha

plt.xlabel('Fecha y hora')
plt.ylabel('Temperatura [oC]')
plt.title(' Sensor Temperatura interior')
plt.plot(df1['time'], df1['value'])

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))   #to get a tick every 3 hours
ax.xaxis.set_major_formatter(xfmt)
plt.plot(df1['time'][df1['value']> 50], df1['value'][df1['value'] > 50], 'bo') #Marcar con un ciruclo (bo= blue o) los puntos por encima de 40
plt.plot(df1['time'][df1['value']< 0], df1['value'][df1['value'] < 0], 'ro')



#VALORES IMPORTANTES
maximo=df1['value'].max()
minimo=df1['value'].min()
media=df1['value'].mean()

#AJUSTAR A VALORES REALES (eliminar cuando se tengan los sensores)
doc=pd.read_csv('Temperatura ext.csv')
df=pd.DataFrame(doc,columns=['row','last_val_time','ave'])
df.rename(columns={'last_val_time':'time','ave':'value'}, inplace=True)
df['value']=df['value'].fillna(method='ffill')

#ANADIMOS COLUMNA VALORES TEMP EXT
tempext=df['value']
df2=df1
df2['Tempext']=tempext

#Condicion de sumar o restar grados si la tempext es superior o inferior a 17 (condicion, valor si se cumple, valor si no se cumple)
df2['value'] = np.where(df2['Tempext']>17, df2['value']+ random.uniform(0.5,1.5), df2['value']- random.uniform(0.5,1.5))



#CREAR ALARMA
#DataFrame de la alarma 1
alarmas1=df2[df2['value'] > 40]
alarmas1['tiposensor']= 'Temperatura'
alarmas1['event']= 'Temperatura H'
del alarmas1['Tempext']

#DataFrame de la alarma 2
alarmas2=df2[df2['value'] < 0]
alarmas2['tiposensor']= 'Temperatura'
alarmas2['event']= 'Temperatura L'
del alarmas2['Tempext']

#Juntamos DataFrames en uno solo
alarmast=alarmas1.append(alarmas2, ignore_index=True)

#Ordenamos las alarmas por tiempo
alarmast=alarmast.sort_values(by='time')


plt.close()