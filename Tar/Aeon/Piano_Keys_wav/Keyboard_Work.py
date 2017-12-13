#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:08:57 2017

@author: xueqianhe
"""

stave_image_filename = 'timg.jpg'
mouse_image_filename = 'yinfu.png'
note_image_filename = 'yinfu2.png'

import pygame
from pygame.locals import *
from sys import exit



#pygame.mixer.pre_init(44100,16,2,4096)
pygame.mixer.init()
pygame.init()
sound40 = pygame.mixer.Sound('40-C4.wav')
sound42 = pygame.mixer.Sound('42-D4.wav')
sound44 = pygame.mixer.Sound('44-E4.wav')
sound45 = pygame.mixer.Sound('45-F4.wav')
sound47 = pygame.mixer.Sound('47-G4.wav')
sound49 = pygame.mixer.Sound('49-A4.wav')
sound51 = pygame.mixer.Sound('51-B4.wav')
sound52 = pygame.mixer.Sound('52-C5.wav')
sound54 = pygame.mixer.Sound('54-D5.wav')
sound56 = pygame.mixer.Sound('56-E5.wav')
sound57 = pygame.mixer.Sound('57-F5.wav')
sound59 = pygame.mixer.Sound('59-G5.wav')

screen = pygame.display.set_mode((900,289), 0, 32)
pygame.display.set_caption("Notesboard")
background = pygame.image.load(stave_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
note_cursor = pygame.image.load(note_image_filename).convert_alpha()
def loop():    
    x = 450
    y = -100
    m = 460
    n = -120
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()       
            if event.type == pygame.KEYDOWN:
                
         #white key
                if event.key == pygame.K_w:
                    
                    sound40.play()
                    x = 170
                    y = 200 
                        
                if event.key == pygame.K_e:
                    sound42.play()
                    x = 210
                    y = 185         
                if event.key == pygame.K_r:
                    sound44.play()
                    x = 250
                    y = 170
                if event.key == pygame.K_t:
                    sound45.play()
                    x = 290
                    y = 145
                if event.key == pygame.K_y:
                    sound47.play()
                    x = 330
                    y = 125
                if event.key == pygame.K_u:
                    sound49.play()
                    x = 370
                    y = 105
                if event.key == pygame.K_i:
                    sound51.play()
                    x = 410
                    y = 85
                if event.key == pygame.K_o:
                    sound52.play()
                    x = 450
                    y = 65
                if event.key == pygame.K_a:
                    sound54.play()
                    x = 490
                    y = 45
                if event.key == pygame.K_s:
                    sound56.play()
                    x = 530
                    y = 25
                if event.key == pygame.K_d:
                    sound57.play()
                    x = 570
                    y = 5
                if event.key == pygame.K_f:
                    sound59.play()
                    x = 610
                    y = -8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_e or event.key == pygame.K_r:
                    x = 450
                    y = -100
                if event.key == pygame.K_t or event.key == pygame.K_y or event.key == pygame.K_u:
                    x = 450
                    y = -100
                if event.key == pygame.K_i or event.key == pygame.K_o or event.key == pygame.K_a:
                    x = 450
                    y = -100
                if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_f:
                    x = 450
                    y = -100   
                        
        screen.blit(background, (0,0))            
        screen.blit(mouse_cursor, (x,y))
        screen.blit(note_cursor,(m,n))
        pygame.display.update()      
loop()
pygame.quit()
quit()
