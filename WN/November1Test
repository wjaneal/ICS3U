#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:49:26 2017

@author: wneal
"""

#Largest (Test Question 1)
def largest(list1): #Create a function - largest
    L = list1[0] #Initialize L, the largest number
    #Set its value to the first item in the list
    for i in range(1,len(list1)):
        #Iterate through all other list items
        if list1[i]>L: #If a new item is larger,
            L = list1[i] #set L to its value
    return L

#CheckForElement - function to determine
#Whether an element is in a list.
def checkForElement(List1,element):
    for i in range(0,len(List1)):
        if List1[i]==element:
            return True #Quit the function, back
            #to main program
    return False
    
#Function to return elements in odd positions
#in a list
def returnOdd(List1):
    newList = []
    #Iterate through all of the elements
    for i in range(0,len(List1)): 
        if i % 2 == 0: #Append the "even" elements
            #because they are odd elements for humans
            newList.append(List1[i])
    return newList
  
def palindrome(string1):
    List1 = []
    for i in string1:
        List1.append(i)
    List2 = List1#Lists should be the same forward and backward
    List2.reverse() #First set List2=List2
    #Then, reverse List2
    #so reverse List2
    if List2 == List1: #If the two lists are equal:
        #Return true
        return True
    return False #Otherwise return false

def integerDigits(number):
    List1 = []
    for i in str(number): #Change the number to a string
        #Each character becomes a list item
        List1.append(int(i)) #Change back to integers
    return List1

def concatenateLists(List1,List2):
    return List1+List2
    #You could append each List2 element to list 1
    #one by one

List1 = [4,6,5,7,6,77,6,7,8,77,8]
List2 = [4,7,8,6,4,66,8,8,6,5,3]
number1 = 53987358

print(largest(List1))
print(checkForElement(List1,77))
print(checkForElement(List2,77))
print(returnOdd(List1))
print(returnOdd(List2))
print(palindrome("ABCBA"))
print(palindrome("ABCDE"))
print (integerDigits(number1))
print(concatenateLists(List1,List2))

