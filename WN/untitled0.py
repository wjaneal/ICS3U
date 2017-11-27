#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:58:52 2017

@author: wneal
"""
from math import *

G = 6.67*10**(-11)

def Fg(G,m,r):
    return G*m/(r*r)

def mass(r,d):
    pi = 4*atan(1)
    V = 4/3*pi*r**3
    return V*d

r1 = 8000000
r2 = 16000000
d1 = 6000
d2 = 3000

print (Fg(G,mass(r1,d1),r1 ))
print (Fg(G,mass(r2,d2),r2 ))