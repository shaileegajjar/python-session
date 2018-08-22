# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:41:47 2018

@author: shaileeg
"""

import math
import pandas as panda
import matplotlib.pyplot as plt

#data_field1 = panda.read_csv('signal_strenght1.csv')
data_field2 = panda.read_csv('gps1.csv')

# Importing the fields to arrays
#signals = data_field1['strenght10']
#time1 = data_field1['time10']

time2 = data_field2['time']
speed = data_field2['speed']
lat = data_field2['lat']
lng = data_field2['lng']

# Visualizing the data
#plot(X,Y,specifiers)
#plt.plot(time2,speed,'b')
plt.plot(time2,speed,'b')
plt.xlabel('Xaxis --> Samples')
plt.ylabel('Yaxis --> Speed')
# Insert title ('My Title - Speed vs Time') ?? 
# Legend ??? 
plt.title('Novi ----- Speed vs Time ')
plt.legend('Speed')
plt.show()

# Analysis and Plotting 

