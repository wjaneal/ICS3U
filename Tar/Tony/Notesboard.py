# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 02:18:57 2017

@author: 11256
"""

stave_image_filename = 'timg.jpg'

import pygame
from pygame.locals import *
from sys import exit
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(10,10)

pygame.init()
screen = pygame.display.set_mode((563,181), 0, 32)
pygame.display.set_caption("Notesboard")
background = pygame.image.load(stave_image_filename).convert()
while True:
        for event in pygame.event.get():
            if event.type == exit:
                exit()
        screen.blit(background, (0,0))
        pygame.display.update()
        