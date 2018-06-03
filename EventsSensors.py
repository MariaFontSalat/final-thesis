import numpy as np
import pandas as pd
import datetime
import  matplotlib.pyplot as plt

df = pd.read_csv('mFievent.csv')

df1 = pd.DataFrame(df,columns=['time','rulename','sensor','sensor_value'])

#ELIMINAR FILAS CON VALORES NaN (corresponden a alertas de conectar o desconectar que no nos interesan)
df1 = df1.dropna(how='any')

df1['time']=df1['time']/1000
df1['time'] = df1['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))

print df1

writer = pd.ExcelWriter('EventsSensorsexport.xlsx')
df1.to_excel(writer,'Sheet1')
writer.save()

plt.close()