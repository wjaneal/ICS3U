# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 01:08:56 2017

@author: fy
"""

import pygame
import time
import random

pygame.init()

beginning_sound = pygame.mixer.Sound("C:\\Users\\fy\\Music\\3426_draeseke_puzzle5-dd000438-fa1e-4f42-8488-399dc77fa412.wav")
#pygame.mixer.music.load("‪C:\\Users\\fy\\Music\\pumped.wav")
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red =(200,0)
green =(0,200,0)

bright_red = (255,0)
bright_green = (0,255,0)

block_color = (53,115,255)

Mario_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Emma's Game")
clock = pygame.time.Clock()

MarioImg = pygame.image.load("C:\\Users\\fy\\Documents\\ICS3U\\TeddyBears\\Emmafinal\\Mario.gif")
gameIcon = pygame.image.load("C:\\Users\\fy\\Documents\\ICS3U\\TeddyBears\\Emmafinal\\icon.gif")

pygame.display.set_icon(gameIcon)

pause = False
#crash = True

def things_dodged(count):
    font = pygame.font.SysFont("serif", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
    
def things(thingx, thingy,thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy,thingw, thingh])
    
def car(x,y):
    gameDisplay.blit(MarioImg,(x,y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def crash():
    
    pygame.mixer.music.stop()
    
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
                
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsanms",20)
    textSurf, textRect = test_objects(msg, smallText)
    textRect.center = ((x+(w/2),(y+(h/2))))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()         
    
def unpause():
    global pause
    pause = False
    
def paused():
    
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
                
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def game_intro():
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)        
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Emma's game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect) 
        
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
        
def game_loop():
    global pause
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
    
    
    