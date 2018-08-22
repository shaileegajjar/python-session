# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:32:26 2018

@author: shaileeg
"""

class Animal:
    
    def __init__(self, name ="No name"):
        self._name = name
        
    def getName(self):
        return self._name
        
lion = Animal()
monkey = Animal("Tarzan")

print(lion.getName())
print(monkey.getName())
