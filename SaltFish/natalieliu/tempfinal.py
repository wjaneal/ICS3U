# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
guess = 0
tries = 0
score = 0
   
print ("welcome to my quiz!")
guess =input("would you like to begin?:")
if guess == "yes":
    print ("good luck")
    

    guess = input("which of the following is an example of a heterotroph?,algae,tiger,moss,flower")
    if guess == "b":
        print ("Good job!")
        score = score + 10
    else:
        print ("no, your worng")
        score = score - 10
    tries = tries + 1
    

    guess =input("what is the color of sky?,blue,red,green")
    if guess == "a":
         print ("good job!")
         score = score + 10
    else:
        print ("no, your worng")
        score = score - 10
    tries = tries + 1
    


    guess =input("in which kingdom are mushrooms classified?,eunacteria,protista,fungi")
    if guess == "c":
         print ("Great")
         score = score + 10
    else:
        print ("no, your worng")
        score = score - 10
    tries = tries + 1

       
    guess =input("which characteristics are shared by fens, dandelions, and maple trees?,no chliroplast,heterotrophic,photosynthetic")
    if guess == "c":  
         print ("you are right!")
         score = score + 10
    else:
        print ("no, your worng")
        score = score - 10
    tries = tries + 1
print ("you score is",score)
print("thanks for playing.")
        
            
            
            
            
