#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:08:57 2017
@author: xueqianhe
"""
stave_image_filename = 'timg8.jpeg'
mouse_image_filename = 'yinfu.png'
note_image_filename = 'yinfu2.png'
piano_image_filename = 'Piano.png'
change_image_filename = 'piano1.png'
change2_image_filename = 'piano2.png'
change3_image_filename = 'piano3.png'
change4_image_filename = 'piano4.png'
import pygame
from pygame.locals import *
from sys import exit
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
sound61 = pygame.mixer.Sound('61-A5.wav')
sound63 = pygame.mixer.Sound('63-B5.wav')

sound41 = pygame.mixer.Sound('41-C4#.wav')
sound43 = pygame.mixer.Sound('43-D4#.wav')
sound46 = pygame.mixer.Sound('46-F4#.wav')
sound48 = pygame.mixer.Sound('48-G4#.wav')
sound50 = pygame.mixer.Sound('50-A4#.wav')
sound53 = pygame.mixer.Sound('53-C5#.wav')
sound55 = pygame.mixer.Sound('55-D5#.wav')
sound58 = pygame.mixer.Sound('58-F5#.wav')
sound60 = pygame.mixer.Sound('58-F5#.wav')
sound62 = pygame.mixer.Sound('62-A5#.wav')
                             
screen = pygame.display.set_mode((900,696), 0, 32)
pygame.display.set_caption("Notesboard")
background = pygame.image.load(stave_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
note_cursor = pygame.image.load(note_image_filename).convert_alpha()
piano_cursor = pygame.image.load(piano_image_filename).convert_alpha()
change_cursor = pygame.image.load(change_image_filename).convert_alpha()
change2_cursor = pygame.image.load(change2_image_filename).convert_alpha()
change3_cursor = pygame.image.load(change3_image_filename).convert_alpha()
change4_cursor = pygame.image.load(change4_image_filename).convert_alpha()

def loop():    
    x,y = 500,-500
    m,n = 500,-500
    p,q = 500,-500
    a,b = 500,-500
    c,d = 500,-500
    f,g = 500,-500
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                pygame.quit()
                quit()       
            if event.type == pygame.KEYDOWN:           
         #white key
                if event.key == pygame.K_q:                  
                    sound40.play()
                    x,y = 160,205
                    p,q = 49,365
                if event.key == pygame.K_w:                  
                    sound42.play()
                    x,y = 210,185
                    a,b = 104,365
                if event.key == pygame.K_e:
                    sound44.play()
                    x,y = 260,161
                    c,d = 159,365
                if event.key == pygame.K_r:
                    sound45.play()
                    x,y = 310,142
                    p,q = 215,365
                if event.key == pygame.K_t:
                    sound47.play()
                    x,y = 360,117
                    a,b = 270,365
                if event.key == pygame.K_y:
                    sound49.play()
                    x,y = 410,95
                    a,b = 325,365
                if event.key == pygame.K_u:
                    sound51.play()
                    x,y = 460,73
                    c,d = 380,365
                if event.key == pygame.K_z:
                    sound52.play()
                    x,y = 510,51
                    p,q = 435,365
                if event.key == pygame.K_x:
                    sound54.play()
                    x,y = 560,29
                    a,b = 490,365
                if event.key == pygame.K_c:
                    sound56.play()
                    x,y = 610,7
                    c,d = 545,365
                if event.key == pygame.K_v:
                    sound57.play()
                    x,y = 660,-15
                    p,q = 601,365
                if event.key == pygame.K_b:
                    sound59.play()
                    x,y = 710,-37
                    a,b = 656,365
                if event.key == pygame.K_n:
                    sound61.play()
                    x,y = 760,-59
                    a,b = 711,365
                if event.key == pygame.K_m:
                    sound63.play()
                    x,y = 810,-81
                    c,d = 766,365
          #black key         
                if event.key == pygame.K_2:
                    sound41.play()
                    m,n = 160,205
                    f,g = 83,367
                if event.key == pygame.K_3:
                    sound43.play()
                    m,n = 210,185
                    f,g = 139,367
                if event.key == pygame.K_5:
                    sound46.play()
                    m,n = 310,142
                    f,g = 250,367
                if event.key == pygame.K_6:
                    sound48.play()
                    m,n = 360,117
                    f,g = 305,367
                if event.key == pygame.K_7:
                    sound50.play()
                    m,n = 410,95
                    f,g = 360,367
                if event.key == pygame.K_s:
                    sound53.play()
                    m,n = 510,51
                    f,g = 470,367
                if event.key == pygame.K_d:
                    sound55.play()
                    m,n = 560,29
                    f,g = 526,367
                if event.key == pygame.K_g:
                    sound58.play()
                    m,n = 660,-15
                    f,g = 636,367
                if event.key == pygame.K_h:
                    sound60.play()
                    m,n = 710,-37
                    f,g = 691,367
                if event.key == pygame.K_j:
                    sound62.play()
                    m,n = 760,-59
                    f,g = 747,367
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_z or event.key == pygame.K_r or event.key == pygame.K_v:
                    x,y = 450,-500
                    p,q = 500,-500 
                if event.key == pygame.K_e or event.key == pygame.K_m or event.key == pygame.K_c or event.key == pygame.K_u:
                    x,y = 450,-500
                    c,d = 500,-500       
                if event.key == pygame.K_w or event.key == pygame.K_t or event.key == pygame.K_y:
                    x,y = 450,-500
                    a,b = 500,-500
                if event.key == pygame.K_b or event.key == pygame.K_n or event.key == pygame.K_x:
                    x,y = 450,-500
                    a,b = 500,-500                                 
                if event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_5:
                    m,n = 500,-500
                    f,g = 500,-500
                if event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_s:
                    m,n = 500,-500
                    f,g = 500,-500
                if event.key == pygame.K_d or event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_j:
                    m,n = 500,-500   
                    f,g = 500,-500
        screen.blit(background, (0,0))            
        screen.blit(mouse_cursor, (x,y))
        screen.blit(note_cursor,(m,n)) 
        screen.blit(piano_cursor,(0,340))
        screen.blit(change_cursor,(p,q))
        screen.blit(change2_cursor,(a,b))
        screen.blit(change3_cursor,(c,d))
        screen.blit(change4_cursor,(f,g))       
        pygame.display.update()      
loop()
pygame.quit()
quit()
