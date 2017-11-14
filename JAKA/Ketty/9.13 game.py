# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 01:49:54 2017

@author: sg
"""

num_players = input("How many players?")
player_names = ["JED"]
for i in range(0,num_players):
    a=raw_input("Your name:")
    player_names.append(a)
for i in range(0,num_players):
    print i+1, player_names[i]
    