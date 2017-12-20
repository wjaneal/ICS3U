#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:39:38 2017

@author: wneal
"""

#Algorithm - specific steps to solve problem
#Sort an array
array = [6,8,5,9,3,7,8,9,1,223,4,3443,5,6677667,5,6]
for repeats in range(0,len(array)-1):
    for i in range(0,len(array)-1):
        if array[i]>array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
        print("Repeat number:", repeats, " i:", i, " array:", array)
print (array)        
