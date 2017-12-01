# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 01:08:56 2017

@author: fy
"""

import pygame
import time
import random

pygame.init()

beginning_sound = pygame.mixer.Sound("‪C:\\Users\\fy\\Music\\DragonCoin.wav")

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

gameDisplay = pygame.display.set_caption("Emma's Game")
clock = pygame.time.Clock()

MarioImg = pygame.image.load("C:\\Users\\fy\\Documents\\ICS3U\\TeddyBears\\Emmafinal\\Mario.gif")
gameIcon = pygame.image.load("C:\\Users\\fy\\Documents\\ICS3U\\TeddyBears\\Emmafinal\\icon.gif")

pygame.display.set_icon(gameIcon)

