# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
with open( 'G:\SNCR\CSV_4_SNCR\H2O_New__ADD_ITL.csv','rb') as f:
    reader = csv.reader(f)
    temperatures=[]
    factors=[]
    NOs=[]
    for row in reader:
       # print(row)
        try:
            Temperature=float(row[1])
            factor=float(row[0])
            NO=float(row[3])
            temperatures.append(Temperature)
            factors.append(factor)
            NOs.append(NO)
        except:
            continue
    s=['s','^','*','p','x','D']
    lgdArry=['0% H2O' ,'2% H2O' ,'4% H2O' ,'6% H2O' ,'8% H2O' ,'10% H2O' ]
    jj=-1
    DataPoint=[]
    for j in [0,1,2,3,4,5]:
        jj=jj+1
        temperature= np.array( [temperatures[i] for i in range(len(factors)) if factors[i]==0.02*j])
        NO_factor_j = np.array([NOs[i]/0.0002 for i in range(len(factors)) if factors[i]==0.02*j])
        f=interp1d(temperature[1:], NO_factor_j[1:],kind='cubic')# the 2 minimum values can not be the same

        temperature_new=np.linspace(temperature[1],temperature[-1],num=90,endpoint=True)
        ltemp,= plt.plot(temperature,NO_factor_j,s[jj],label=lgdArry[jj],markersize=6)
        DataPoint.append(ltemp)
        plt.plot( temperature_new,f(temperature_new),'--')
        plt.show()
       # plt.hold(True)
plt.xlabel('Temperature ($^\circ$C)',fontsize='large')
plt.ylabel('NO out/ NO in',fontsize='large')
plt.legend(handles=DataPoint,fontsize='large')
