#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:48:51 2017

@author: Yolanda
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:02:31 2017

@author: Yolanda
"""

"""
This is drawing board that allows you to draw whatever you want.
Sorry, I thought in the list,list1[0]should be the x-axis and list1[1]should be the y -axis. 
However, when I set the direction of the line in this way, the line just doesn't go down or go up.
"""

import random
import pygame
import sys
from pygame.locals import *

FPS = 15 # Assign the basic window
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

# Use RGB to get the colour.   
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
YELLOW = (  0, 155,   0)
GREY  = ( 40,  40,  40)
BGCOLOR = BLACK

#Assign the direction of movement.
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # The index of snake's head

def main(): # The main window.
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('DRAW')

    showStartScreen() 
    while True: #While loop to run the game.
        runGame()

def drawGrid(): # Set the whole as a coordinate to express the position much more easily.
    for x in range(0, WINDOWWIDTH, 20): # The vertical lines(y-axis).
        pygame.draw.line(DISPLAYSURF, GREY, (x, 0), (x, WINDOWHEIGHT)) # The origin start at the bottom left.
    for y in range(0, WINDOWHEIGHT, 20): # The horizontal lines(x-axis).
        pygame.draw.line(DISPLAYSURF, GREY, (0, y), (WINDOWWIDTH, y))

def runGame():
    direction = RIGHT
    # Set a random start point as the start.
    list1 = [45,123,55]
    while True: # main game loop
        for event in pygame.event.get(): # Event loop.
            if event.type == QUIT: # Restart.
                terminate()
            # Use up, down, left and right key to control the movement of snake:
            elif event.type == KEYDOWN: 
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT: # Press left key to turn left.
                    direction = LEFT
                    list1[0] -=5
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT: # Press right key to turn right.
                    direction = RIGHT
                    list1[0] +=5
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN: # Press up key to go up.
                    direction =  UP
                    list1[1] +=5
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP: # Press down key to go down.
                    direction = DOWN
                    list1[1] -=5
                elif event.key == K_ESCAPE: # Command and space to suspend the game.
                    terminate()
        drawShape(list1)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        
def drawPressKeyMsg(): # The window to start the game by pressing a key.
    pressKeySurf = BASICFONT.render('Press a key to play.', True, GREY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress(): # Check if the event is less than the maximum.
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen(): # Show the welcome window.
    titleFont = pygame.font.Font('freesansbold.ttf', 80)
    titleSurf = titleFont.render('Let us Draw', True, WHITE, YELLOW)

    degrees = 0 # At first, this line should be horizontal.
    while True:
        DISPLAYSURF.fill(BGCOLOR) 
        rotatedSurf = pygame.transform.rotate(titleSurf, degrees)
        rotatedRect = rotatedSurf.get_rect()
        rotatedRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2) # Set the line at the centre.
        DISPLAYSURF.blit(rotatedSurf, rotatedRect)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear events.
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees += 5 # Change the degree to rotate the line.


def terminate(): # Terminate to stop or suspend the game.
    pygame.quit()
    sys.exit()


def drawShape(list1):
    for i in range(0,len(list1)):
        Rects = pygame.Rect(list1[i]+i,40+i,list1[i],60+i)
        pygame.draw.rect(DISPLAYSURF, RED, Rects )


if __name__ == '__main__':
    main()