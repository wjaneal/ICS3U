# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:30:00 2017
@author: Tommy Li
"""

num_players = input("How many players ")
player_names = []
for i in range(0,num_players):
    a=raw_input("please type player name here ")
    player_names.append(a)

num_rounds = 9
money = 5000
for round in range(0,num_rounds):
    print "It is round ", round+1
    for player in range(0,len(player_names)):
        print player_names[player], " it is your turn now."
        answer = ""
        while answer != "F":
            answer = raw_input("Type 'B' to buy, 'S' to sell and 'F' if you finished")
            if answer == "B":
                 print"buying succeed，minus 500 ."
                 money = money - 500
            if answer == "S":
                 print"Selling cuccessed , add 400 . "  
                 money = money + 400
print "Your total money is: "
print money , 
print "out of ", num_rounds, " questions correct."
print"The game is over,thank you for playing！！！！"