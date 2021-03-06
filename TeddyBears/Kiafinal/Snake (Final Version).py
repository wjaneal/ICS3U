# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:03:23 2017

@author: Kia
"""
#importing curses and having a terminal to desplay game
import random
import curses

s = curses.initscr()
curses.curs_set(0) #Set the cursor state and setting visibility on (0)
sh, sw = s.getmaxyx()     #sh for sanke's hight and sw for sanke's width and getting them from get max       
w = curses.newwin(sh, sw, 0, 0)    #coding prepartion if snake moves and having a new window
w.keypad(1)
w.timeout(5) #Timeout for setting the speed of snake #Paint character snake at (y, x)
snk_x = int(sw/4)   #x is gonna be width divided by 4
snk_y = int(sh/2)   #y is gonna be height divided by 2
snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
]

food = [int(sh/2), int(sw/2)] #put the food at the center of the screen
w.addch(int(food[0]), int(food[1]), curses.ACS_DIAMOND) #shaping food as a Diamond using ACS code #Adding a new charecter with .addch

key = curses.KEY_RIGHT
#Using a while loop
while True:
    next_key = w.getch() #Get a character and .getch makes it wait till key be pressed #it moves snake depends on the pressed key 
    key = key if next_key == -1 else next_key
    #These codes are preventing snake for going backward and if player press a key for going backward, game will be stoped
    if snake [0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]: #the player can lose if the snake hit the top, down, left or right of the screen
        curses.endwin()  #so its going to kill the window                          #or if snake is itself
        quit()         #and quit
        
    new_head = [snake[0][0],snake[0][1]]
    #if statement for controlling snake on keyboard
    if key == curses.KEY_DOWN:       #Using key constants and relate it to Keystroke
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1 
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
        
    snake.insert(0, new_head)
    #When snake reach food, food will be somewhere else randomly
    if snake[0] == food:
        food = None     #so food is none it will create another food
        while food is None:
            nf = [
            random.randint(1, sh-1),   #these codes make the food randomly
            random.randint(1, sw-1)
            ]
            #food has to be anywhere expect on snake's range
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')
    #adding the head of snake to the screen using CKboard
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)