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
This is a Slither game called "Hungry Snake". Player use key left, right, up 
and down to control the motion of snake and let it eat the fruit and avoiding
running into the wall or itself.
"""

import random
import pygame
import sys
from pygame.locals import *

FPS = 15 # Assign the basi window
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FRUITSIZE = 20 # Assign the fruit.
assert WINDOWWIDTH % FRUITSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % FRUITSIZE == 0, "Window height must be a multiple of cell size."
FRUITWIDTH = int(WINDOWWIDTH / FRUITSIZE)
FRUITHEIGHT = int(WINDOWHEIGHT / FRUITSIZE)

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
    pygame.display.set_caption('SNAKE')

    showStartScreen() 
    while True: #While loop to run the game.
        runGame()
        showGameOverScreen()


def runGame():
    # Set a random start point as the start.
    startx = random.randint(5, FRUITWIDTH - 6)
    starty = random.randint(5, FRUITHEIGHT - 6)
    snakeTrail = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    # Start the fruit in a random place.
    fruit = getRandomLocation()

    while True: # main game loop
        for event in pygame.event.get(): # Event loop.
            if event.type == QUIT: # Restart.
                terminate()
            # Use up, down, left and right key to control the movement of snake:
            elif event.type == KEYDOWN: 
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT: # Press left key to turn left.
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT: # Press right key to turn right.
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN: # Press up key to go up.
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP: # Press down key to go down.
                    direction = DOWN
                elif event.key == K_ESCAPE: # Command and space to suspend the game.
                    terminate()

        # check if the snake has run into the wall
        if snakeTrail[HEAD]['x'] == -1 or snakeTrail[HEAD]['x'] == FRUITWIDTH or snakeTrail[HEAD]['y'] == -1 or snakeTrail[HEAD]['y'] == FRUITHEIGHT:
            return # game over
        for snakeBody in snakeTrail[1:]:
            if snakeBody['x'] == snakeTrail[HEAD]['x'] and snakeBody['y'] == snakeTrail[HEAD]['y']:
                return # game over

        # check if the snake has eaten a fruit.
        if snakeTrail[HEAD]['x'] == fruit['x'] and snakeTrail[HEAD]['y'] == fruit['y']:
            # Snake's tail should not be moved.
            fruit = getRandomLocation() # Set a new fruit in a random place.
        else:
            del snakeTrail[-1] # Remove the tail now to change the length.

        # Add the segment to the direction of the snake moving to let it go further.
        if direction == UP:
            newHead = {'x': snakeTrail[HEAD]['x'], 'y': snakeTrail[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snakeTrail[HEAD]['x'], 'y': snakeTrail[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snakeTrail[HEAD]['x'] - 1, 'y': snakeTrail[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': snakeTrail[HEAD]['x'] + 1, 'y': snakeTrail[HEAD]['y']}
        snakeTrail.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawSnake(snakeTrail)
        drawFruit(fruit)
        drawScore(len(snakeTrail) - 3)
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
    titleSurf = titleFont.render('HungrySnake', True, WHITE, YELLOW)

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


def getRandomLocation(): # Create a random location.
    return {'x': random.randint(0, FRUITWIDTH - 1), 'y': random.randint(0, FRUITHEIGHT - 1)}


def showGameOverScreen(): # The window of "Game Over".
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10) # Get the location of line "Game Over".
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out keys

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear events
            return # Quit.

def drawScore(score): # Show the finale score of the player.
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawSnake(snakeTrail): # Draw the hungry snake on the screen. Set the appearance.
    for trail in snakeTrail:
        x = trail['x'] * FRUITSIZE
        y = trail['y'] * FRUITSIZE
        snakeSegmentRect = pygame.Rect(x, y, FRUITSIZE, FRUITSIZE)
        pygame.draw.rect(DISPLAYSURF, YELLOW, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, FRUITSIZE - 8, FRUITSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, snakeInnerSegmentRect)


def drawFruit(trail): # Draw the fruit on the screen. Set the appearance.
    x = trail['x'] * FRUITSIZE
    y = trail['y'] * FRUITSIZE
    fruitRect = pygame.Rect(x, y, FRUITSIZE, FRUITSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, fruitRect)


def drawGrid(): # Set the whole as a coordinate to express the position much more easily.
    for x in range(0, WINDOWWIDTH, FRUITSIZE): # The vertical lines(y-axis).
        pygame.draw.line(DISPLAYSURF, GREY, (x, 0), (x, WINDOWHEIGHT)) # The origin start at the bottom left.
    for y in range(0, WINDOWHEIGHT, FRUITSIZE): # The horizontal lines(x-axis).
        pygame.draw.line(DISPLAYSURF, GREY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()