# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:20:43 2017

@author: callm
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
txtDisplay.pack( side = TOP)

button1 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="C# ", bg="black",fg="white",command=value_Cs)
button1.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button2 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="D# ", bg="black",fg="white",command=value_Ds)
button2.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)

button3 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="F# ", bg="black",fg="white",command=value_Fs)
button3.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button4 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="G# ", bg="black",fg="white",command=value_Gs)
button4.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)

button2 = Button(topframe,padx=8, pady=8, height = 6, bd=8, text"Bb ", bg="black",fg="white",command=value_Bb)
button2.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=4, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button3 = Button(topframe,padx=8, pady=8, height = 6, bd=8, text"C#1 ", bg="black",fg="white",command=value_Cs1)
button3.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=4, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button4 = Button(topframe,padx=8, pady=8, height = 6, bd=8, text"D#1 ", bg="black",fg="white",command=value_Ds1)
button4.pack(side =LEFT)


frame1 = Frame(root)
frame1.pack( side = TOP )

button1 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="C",fg="black",command=value_C)
button1.pack(side =LEFT)
button2 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="D",fg="black",command=value_D)
button2.pack(side =LEFT)
button3 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="E",fg="black",command=value_E)
button3.pack(side =LEFT)
button4 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="F",fg="black",command=value_F)
button4.pack(side =LEFT)

button5 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="G",fg="black",command=value_G)
button5.pack(side =LEFT)
button6 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="A",fg="black",command=value_A)
button6.pack(side =LEFT)
button7 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="B",fg="black",command=value_B)
button7.pack(side =LEFT)
button8 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="C1",fg="black",command=value_C1)
button8.pack(side =LEFT)
