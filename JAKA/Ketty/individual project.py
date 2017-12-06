import random

print ("Let's start our games! Which one do you want to play?")
kind = input("You can choose:1.SRP 2.guess numbers")

if kind == "1":
    j = int(input("How many rounds do you want to play?"))
    c = 0
    d = 0
    e = 0
    for i in range(0,j):
        print ("Round",i+1,":")
        a = input("Scissors, Rock and Paper! Your choice:")
        b = int(random.random()*3)
        if a == "S" or a == "s":
            a = 0
        if a == "R" or a == "r":
            a = 1
        if a == "P" or a == "p":
            a = 2
        if a == 0 and b == 1:
            print ("Your choice is scissors, computer's choice is rock. You lose!")
            c+=1
        if a == 0 and b == 2:
            print ("Your choice is scissors, computer's choice is paper. You win!")
            d+=1
        if a == 1 and b == 0:
            print ("Your choice is rock, computer's choice is scissors. You win!")
            d+=1
        if a == 1 and b == 2:
            print ("Your choice is rock, computer's choice is paper. You lose!")
            c+=1
        if a == 2 and b == 0:
            print ("Your choice is paper, computer's choice is scissors. You lose!")
            c+=1
        if a == 2 and b == 1:
            print ("Your choice is paper, computer's choice is rock. You win!")
            d+=1
        if a == b:
            print ("This round is a Draw!")
            e+=1
    print("You played", j,"rounds and you win for",d,"times, lose for",c ,"and ",e," Draws!")
        
if kind == "2":
    print("Let's guess the number! The range is from 1 to 100.")
    a=int(random.random()*100)+1
    c=1
    b=int(input("Guess a number:"))
    while b!=a:
        if b>a:
            c+=1
            print("your answer is greater than the number!")
            b=int(input("Guess a number:"))
        if b<a:
            c+=1
            print("your answer is smaller than the number!")
            b=int(input("Guess a number:"))
    print ("Congradulations! You spend",c,"times to guess the correct number!!")
