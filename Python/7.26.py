# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:09:57 2018

@author: shaileeg
"""

import math
import pandas as panda
import matplotlib.pyplot as plt

data_field1 = panda.read_csv('123.csv')

#time = data_field1['x']
speed = data_field1['sensor_data']
#lat = data_field2['lat']
#lng = data_field2['lng']

# Visualizing the data
#plot(X,Y,specifiers)
#plt.plot(time1,speed,'b')
#plt.plot(time,speed,'g')
plt.plot(speed,'r')
plt.xlabel('Xaxis --> Samples')
plt.ylabel('Yaxis --> Speed')
# Insert title ('My Title - Speed vs Time') ?? 
# Legend ??? 
plt.title('Novi ----- Speed vs Time ')
plt.legend('Speed')
plt.show()
