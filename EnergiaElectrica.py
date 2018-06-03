import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import matplotlib.dates as mdates
import math

doc3=pd.read_csv('Energia Electrica.csv')
df4=pd.DataFrame(doc3,columns=['row','last_val_time','salida1','salida2','salida3', 'salida4', 'salida5', 'salida6','salida7', 'salida8'])
df4.rename(columns={'last_val_time':'time','ave':'value'}, inplace=True)

#EPOCH TO HUMAN
df4['time']=df4['time']/1000
df4['time'] = df4['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))

#COMPLETAR CAMPOS VACIOS (con el valor anterior)
df4['salida1']=df4['salida1'].fillna(method='ffill')
df4['salida2']=df4['salida2'].fillna(method='ffill')
df4['salida3']=df4['salida3'].fillna(method='ffill')
df4['salida4']=df4['salida4'].fillna(method='ffill')
df4['salida5']=df4['salida5'].fillna(method='ffill')
df4['salida5']=df4['salida5'].fillna(method='ffill')
df4['salida6']=df4['salida6'].fillna(method='ffill')
df4['salida7']=df4['salida7'].fillna(method='ffill')
df4['salida8']=df4['salida8'].fillna(method='ffill')

#GRAFICAR SENSORES
fig, ax = plt.subplots()
fig.autofmt_xdate()                     #Para adaptar indice x a formato fecha

plt.xlabel('Fecha y hora')
plt.ylabel('Volatje VAC')
plt.title('Sensor mPower')
plt.plot(df4['time'], df4['salida1'], color='red')
plt.plot(df4['time'], df4['salida2'], color='blue')
plt.plot(df4['time'], df4['salida3'], color='green')
plt.plot(df4['time'], df4['salida4'], color='yellow')
plt.plot(df4['time'], df4['salida5'], color='orange')
plt.plot(df4['time'], df4['salida6'], color='pink')
plt.plot(df4['time'], df4['salida7'], color='black')
plt.plot(df4['time'], df4['salida8'], color='brown')

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))   #to get a tick every 3 hours
ax.xaxis.set_major_formatter(xfmt)


#VALORES IMPORTANTES

maximo1=df4['salida1'].max()
minimo1 =df4['salida1'].min()
media1=df4['salida1'].mean()

maximo2=df4['salida2'].max()
minimo2=df4['salida2'].min()
media2=df4['salida2'].mean()

maximo3=df4['salida3'].max()
minimo3 =df4['salida3'].min()
media3=df4['salida3'].mean()

maximo4=df4['salida4'].max()
minimo4 =df4['salida4'].min()
media4=df4['salida4'].mean()

maximo5=df4['salida5'].max()
minimo5 =df4['salida5'].min()
media5=df4['salida5'].mean()

maximo6=df4['salida6'].max()
minimo6 =df4['salida6'].min()
media6=df4['salida6'].mean()

maximo7=df4['salida7'].max()
minimo7 =df4['salida7'].min()
media7=df4['salida7'].mean()

maximo8=df4['salida8'].max()
minimo8 =df4['salida8'].min()
media8=df4['salida8'].mean()

#Determinar el max/min/media global (toda la regleta)
list1=[maximo1,maximo2,maximo3,maximo4,maximo5,maximo6,maximo7,maximo8]
list2=[minimo1,minimo2,minimo3,minimo4,maximo5,minimo6,minimo7,minimo8]
list3=[media1,media2,media3,media4,media5,media6,media7,media8]

def maximo(list):
    maxnum=0
    for num in list:
        if num > maxnum:
            maxnum=num
        else:
            maxnum=maxnum
    return maxnum

#print maximo(list1)

def minimo(list):
    minnum=list[0]
    for num in list:
        if num< minnum:
            minnum=num
        else:
            minnum=minnum
    return minnum

#print minimo(list2)

def media(list):
    suma=0
    for num in list:
        suma=suma+num

    return suma/len(list)


#CREAR ALARMA
#DataFrame de la alarma 1
alarmas4=df4[(df4['salida1'] > 125)]
alarmas4['value']=df4['salida1']
alarmas4['salida']='1'

alarmas5=df4[(df4['salida2'] > 125)]
alarmas5['value']=df4['salida2']
alarmas5['salida']='2'

alarmas6=df4[(df4['salida3'] > 125)]
alarmas6['value']=df4['salida3']
alarmas6['salida']='3'

alarmas7=df4[(df4['salida4'] > 125)]
alarmas7['value']=df4['salida4']
alarmas7['salida']='4'

alarmas8=df4[(df4['salida5'] > 125)]
alarmas8['value']=df4['salida5']
alarmas8['salida']='5'

alarmas9=df4[(df4['salida6'] > 125)]
alarmas9['value']=df4['salida6']
alarmas9['salida']='6'

alarmas10=df4[(df4['salida7'] > 125)]
alarmas10['value']=df4['salida7']
alarmas10['salida']='7'

alarmas11=df4[(df4['salida8'] > 125)]
alarmas11['value']=df4['salida8']
alarmas11['salida']='8'

#Juntamos DataFrames
alarmase=alarmas4.append(alarmas5, ignore_index=True)
alarmase=alarmase.append(alarmas6, ignore_index=True)
alarmase=alarmase.append(alarmas7, ignore_index=True)
alarmase=alarmase.append(alarmas8, ignore_index=True)
alarmase=alarmase.append(alarmas9, ignore_index=True)
alarmase=alarmase.append(alarmas10, ignore_index=True)
alarmase=alarmase.append(alarmas11, ignore_index=True)

alarmase['tiposensor']= 'mPower'
alarmase['event']= 'Voltaje H'


#DataFrame de la alarma 2
#alarmas2=df4[(10 < df4['salida1'] < 110) |  (10 < df4['salida2'] < 110) |  (10 < df4['salida3'] < 110) |  (10 < df4['salida4'] < 110) |  (10 < df4['salida5'] < 110) |  (10 < df4['salida6'] < 110) |  (10 < df4['salida7'] < 110) |  (10 < df4['salida8'] < 110)]
alarmas12=df4[(df4['salida1'] < 110)]
alarmas12['value']=df4['salida1']
alarmas12['salida']='1'

alarmas13=df4[(df4['salida2'] < 110)]
alarmas13['value']=df4['salida2']
alarmas13['salida']='2'

alarmas14=df4[(df4['salida3'] < 110)]
alarmas14['value']=df4['salida3']
alarmas14['salida']='3'

alarmas15=df4[(df4['salida4'] < 110)]
alarmas15['value']=df4['salida4']
alarmas15['salida']='4'

alarmas16=df4[(df4['salida5'] < 110)]
alarmas16['value']=df4['salida5']
alarmas16['salida']='5'

alarmas17=df4[(df4['salida6'] < 110)]
alarmas17['value']=df4['salida6']
alarmas17['salida']='6'

alarmas18=df4[(df4['salida7'] < 110)]
alarmas18['value']=df4['salida7']
alarmas18['salida']='7'

alarmas19=df4[(df4['salida8'] < 110)]
alarmas19['value']=df4['salida8']
alarmas19['salida']='8'

#Juntamos DataFrames

alarmase2=alarmas12.append(alarmas13, ignore_index=True)
alarmase2=alarmase2.append(alarmas14, ignore_index=True)
alarmase2=alarmase2.append(alarmas15, ignore_index=True)
alarmase2=alarmase2.append(alarmas16, ignore_index=True)
alarmase2=alarmase2.append(alarmas17, ignore_index=True)
alarmase2=alarmase2.append(alarmas18, ignore_index=True)
alarmase2=alarmase2.append(alarmas19, ignore_index=True)

alarmase2['tiposensor']= 'mPower'
alarmase2['event']= 'Voltaje L'


#Juntamos DataFrames en uno solo
alarmase3=alarmase.append(alarmase2, ignore_index=True)
print alarmase3

del alarmase3['salida1']
del alarmase3['salida2']
del alarmase3['salida3']
del alarmase3['salida4']
del alarmase3['salida5']
del alarmase3['salida6']
del alarmase3['salida7']
del alarmase3['salida8']


#Ordenamos las alarmas por tiempo
alarmase3=alarmase3.sort_values(by='time')


plt.close()
