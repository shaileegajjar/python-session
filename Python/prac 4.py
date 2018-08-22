# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:06:18 2018

@author: shaileeg
"""
"""
print ("    *  ")
print ("  * * *")
print ("* * * * *")
"""
"""
x = 1
while x<4:
    print(x)
    x=x+1
"""    
    
array = [[5,10,3],
         [3,8,53],
         [4,49]]

for row in range(len(array)):
    for col in range(len(array[row])):
        print(array[row][col], end=" ")
        
print("\n\n*****\n")

for row in reversed(range(len(array))):
    for col in reversed(range(len(array[row]))):
        print(array[col][row], end="\n")

print()

def my_func (country = "India"):
    print(country)
    
country = "Spain"   
my_func()

