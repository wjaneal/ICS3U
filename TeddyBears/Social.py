# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:44:22 2017

@author: Teddy Bears
"""

import pygame
import sys
from tkinter import *

pygame.init()

def value_Cs():
    num1.set("C#")
    sound = pygame.mixer.Sound("C:\\Users\\fy\\Music\\aiyucheng.mp3")
    sound.play()
    return
root = Tk()
frame = Frame(root)
frame.pack()

root.title('BIANO')

num1=StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay=Entry(frame, textvariable = num1, bd=20, insertwidth =1, font=30, justify="center", width=4,)


