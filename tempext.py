import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import matplotlib.dates as mdates

doc=pd.read_csv('Temperatura ext.csv')
df=pd.DataFrame(doc,columns=['row','last_val_time','ave'])
df.rename(columns={'last_val_time':'time','ave':'value'}, inplace=True)


#EPOCH TO HUMAN
df['time']=df['time']/1000
df['time'] = df['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))

#COMPLETAR CAMPOS VACIOS (con el valor anterior)
df['value']=df['value'].fillna(method='ffill')

#GRAFICAR SENSORES
fig, ax = plt.subplots()
fig.autofmt_xdate()                     #Para adaptar indice x a formato fecha

plt.xlabel('Fecha y hora')
plt.ylabel('Temperatura [oC')
plt.title('Sensor Temperatura exterior')
plt.plot(df['time'], df['value'])

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))   #to get a tick every 3 hours
ax.xaxis.set_major_formatter(xfmt)



#VALORES IMPORTANTES
maximo=df['value'].max()
minimo=df['value'].min()
media=df['value'].mean()


plt.close()


