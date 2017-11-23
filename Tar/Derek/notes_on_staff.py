#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:57:52 2017

@author: yuyangchen
"""

stave_image_filename = 'timg.jpg'
mouse_image_filename = 'yinfu.png'

import pygame
from pygame.locals import *
from sys import exit
#click(10,10)

pygame.init()
screen = pygame.display.set_mode((563,181), 0, 32)
pygame.display.set_caption("Notesboard")
background = pygame.image.load(stave_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
while True:
        for event in pygame.event.get():
            if event.type == exit:
                exit()
                
        screen.blit(background, (0,0))
        x,y = pygame.mouse.get_pos()
        x-= mouse_cursor.get_width() / 2
        y-= mouse_cursor.get_height() / 2

        screen.blit(mouse_cursor, (x,y))
        
        pygame.display.update()

                
        
        
