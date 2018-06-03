import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tempext import df
from CurrentSensors import df1
from tempint import df2
from humedad import df3
from EnergiaElectrica import df4


#RELACION CORRIENTE Y TEMPINT
corriente=df1.ix[:,5]
long= len(df1['ave'])-1
temp=df2['value'].ix[:long]

print np.corrcoef(corriente,temp)

plt.subplot(1,2,1)
plt.scatter(corriente,temp)
plt.title('Corriente y temperatura interior')
plt.ylabel('Tint')
plt.xlabel('Corriente')
plt.axis([0, 20, -20,70])


#RELACION TEMPEXT Y TEMPINT

tempexte=df.ix[:,2]

long1=len(tempexte)-1
tempint=df2['value'].ix[:long1]

print np.corrcoef(tempexte,tempint)

plt.subplot(1,2,2)
plt.scatter(tempexte,tempint)
plt.title('Text y Tint')
plt.ylabel('Tint')
plt.xlabel('Text')
plt.axis([-10,50,-20,70])

plt.close()

