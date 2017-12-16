#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:41:42 2017

@author: haichunkan
"""

#import random
class eco():
    def __init__(self,species):
        
        self.species=input("species:")
        
    def Species(self):    
        return self.species
  
class animals(eco):
    def __init__(self,species,prey,predator):
        eco.__init__(self,species)
        self.prey= input("prey:")
        self.predator= input("predator:")
    def Prey(self):
        return self.prey
    def Predator(self):
        return self.predator
    
class plants(eco):
    def __init__(self,species,grow,amount,grasseater):
        eco.__init__(self,species)
        self.grow= int(input("growing rate(1.0-2.0):"))
        self.grasseater= input("grasseater:")
        self.amount= int(input("amount:"))
    def Growingrate(self):
        return self.grow
    def Grasseater(self):
        return self.grasseater
    def Amount(self):
        self.amount*=self.grow
        return self.amount    
    
    
#def Hunting(animals):
    #years=input("years:")
    #for i in range(0,365*years):
        
ele=plants("","","","") 
print (ele.Grasseater(),ele.Amount())       
        