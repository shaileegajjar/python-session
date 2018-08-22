# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:15:23 2018

@author: shaileeg
"""

b = 0
r = 3
for i in range(1, r+1):
    for space in range(1, (r-i)+1):
        print(end="  ")
    while b != (2*i-1):
        print("*", end=" ")
        b = b + 1
    b = 0
    print()


