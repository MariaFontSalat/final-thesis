import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import matplotlib.dates as mdates
import math

doc2=pd.read_csv('Humedad.csv')
df3=pd.DataFrame(doc2,columns=['row','last_val_time','ave'])
df3.rename(columns={'last_val_time':'time','ave':'value'}, inplace=True)

#EPOCH TO HUMAN
df3['time']=df3['time']/1000
df3['time'] = df3['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))

#COMPLETAR CAMPOS VACIOS (con el valor anterior)
df3['value']=df3['value'].fillna(method='ffill')


#GRAFICAR SENSORES
fig, ax = plt.subplots()
fig.autofmt_xdate()                     #Para adaptar indice x a formato fecha

plt.xlabel('Fecha y hora')
plt.ylabel('Humedad Relativa (%)')
plt.title('Sensor Humedad')
plt.plot(df3['time'], df3['value'])

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))   #to get a tick every 3 hours
ax.xaxis.set_major_formatter(xfmt)
plt.plot(df3['time'][df3['value']> 55], df3['value'][df3['value'] > 55], 'bo') #Marcar con un ciruclo (bo) los puntos por encima de 40
plt.plot(df3['time'][df3['value']< 30], df3['value'][df3['value'] <30], 'ro') #Marcar con un ciruclo (bo) los puntos por encima de 40



#VALORES IMPORTANTES
maximo=df3['value'].max()
minimo=df3['value'].min()
media=df3['value'].mean()


#CREAR ALARMA
#DataFrame de la alarma 1
alarmas1=df3[df3['value'] > 55]
alarmas1['tiposensor']= 'Humedad'
alarmas1['event']= 'Humedad H'

#DataFrame de la alarma 2
alarmas2=df3[df3['value'] < 30]
alarmas2['tiposensor']= 'Humedad'
alarmas2['event']= 'Humedad L'

#Juntamos DataFrames en uno solo
alarmash=alarmas1.append(alarmas2, ignore_index=True)


#Ordenamos las alarmas por tiempo
alarmash=alarmash.sort_values(by='time')


plt.close()