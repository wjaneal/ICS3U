# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:20:43 2017

@author: callm
"""
#Group Final Project Plan
#Project Topic:Piano
#Group name: Teddy Bears
#Notes:The players will see the keys of a piano once they open the file.
      #Use the mouse to click the key in order to make a sound.

#import required sources
import pygame
import sys
import tkinter 
from tkinter import *
pygame.init()

Notes = ["c1.wav", "d1.wav", "f1.wav", "g1.wav", "b1.wav", "c1s.wav", "d1s.wav", "c#.wav"]
#Functions that sets the key tone
Tunes = ["C#","D#","F#","G#","Bb","C#1","D#1","C","D","E","F","G","A","B","C1","D1","E1","F1"]
def values(note): #Note is the index of the list "Notes"
    #use list for num1.set()
    for i in range(0,len(Tunes)):
        num1.set(Tunes[i])
    #use list for sound =
    for i in range(0,len(Notes)):
        sound = pygame.mixer.Sound(Notes[i])
        sound.play()
        return

def play_a_tune():
    #Commands to play a set of notes
    #Make sound files in a list
    Notes = ["c#.wav","c1s.wav","d1s.wav","b1.wav","c1.wav","d1.wav","f1.wav","g1.wav"]
    Delays = [250,250,125,125,250,250]
    for i in range(0,len(Notes)):
        sound = pygame.mixer.Sound(Notes[i])
        sound.play()
        #Make a delay in milliseconds from Delays[i]
        pygame.time.delay(Delays[i])
'''        
def play_back_a_tune():
    #playback = []
    #First, call play a tune
    #while len(playback < len(Notes))        
        #check for a pygame event
            #If it is Button for c#:
                #append 0 to the playback list
                #If it is Button for c1s:
                #append 1 to the playback list
            #when done, if playback == Song:
            #print "Yay~"
            #otherwise:
            #print "No WaY"
    #Commands to play notes and have user play them back
    #Respond with correct or incorrect
'''    
root = Tk()
frame = Frame(root)
frame.pack()
root.title('PIANO')
num1=StringVar()
topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay=Entry(frame, textvariable = num1, bd=20, insertwidth =1, font=30, justify="center", width=4,)
txtDisplay.pack( side = TOP)
#Apperance of the keyboard
#declare buttons = []
buttons = []
#for i in range(......):
for i in range(0,len(Notes)):
    #buttons.append(Button(.....))
    buttons.append(Button(topframe,padx=8, height = 6, pady=8, bd=8, text="C# ", bg="black",fg="white",command=values(i)))
    #pack buttons
    buttons[i].pack(side =LEFT)
    '''
button1 = Button(topframe,padx=8, height = 6, pady=8, bd=8, text="C# ", bg="black",fg="white",command=value_Cs) #command = values(0)
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
button2 = Button(topframe,padx=8, pady=8, height = 6, bd=8, text="Bb ", bg="black",fg="white",command=value_Bb)
button2.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=4, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button3 = Button(topframe,padx=8, pady=8, height = 6, bd=8, text="C#1 ", bg="black",fg="white",command=value_Cs1)
button3.pack(side =LEFT)
button22 = Button(topframe, state=DISABLED, height = 7, width=4, padx=0, pady=0, relief=RIDGE)
button22.pack(side =LEFT)
button4 = Button(topframe,padx=8, pady=8, height = 6, bd=8, text="D#1 ", bg="black",fg="white",command=value_Ds1)
button4.pack(side =LEFT)
'''
buttonnew = Button(topframe,padx=8, pady=8, height = 6, bd=8, text="PLAY A TUNE ", bg="black",fg="white",command=play_a_tune)
buttonnew.pack(side =LEFT)
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

button9 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="D1",fg="black",command=value_D1)
button9.pack(side =LEFT)
button10 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="E1",fg="black",command=value_E1)
button10.pack(side =LEFT)
button11 = Button(frame1,padx=16, pady=16, bd=8,height = 8, text="F1",fg="black",command=value_F1)
button11.pack(side =LEFT)

root.mainloop()

# -*- coding: utf-8 -*-
"""

Created on Fri Dec  8 13:36:56 2017

@author: fy
"""

"""

GROUP FINAL EMMA:  sorting_animation.py

A minimal sorting algorithm animation:
Sorts a shelf of 10 blocks using insertion
sort, selection sort and quicksort.

Shelfs are implemented using builtin lists.

Blocks are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press space button
 ---------------------------------------

# Import required modules
from turtle import * 
import random
import os
os.system("C:\\Users\\fy\\Music\\Justin Mahar - Pumped.mp3")


class Block(Turtle):

    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(size * 1.5, 1.5, 2) # square-->rectangle
        self.fillcolor("black")
        self.st()
#Highlight the block which is moving  
    def glow(self):
        self.fillcolor("pink")
#If the block moves in correct order, it turns red.      
    def unglow(self):
        self.fillcolor("red")

    def __repr__(self):
        return "Block size: {0}".format(self.size)


class Shelf(list):

    def __init__(self, y):
        "create a shelf. y is y-position of first block"
        self.y = y
        self.x = -160

    def push(self, d):
        width, _, _ = d.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def _close_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

    def _open_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def pop(self, key):
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def insert(self, key, b):
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()
#Design about specific movements for all 4 sorts
def isort(shelf):
    length = len(shelf)
    for i in range(1, length):
        hole = i
        while hole > 0 and shelf[i].size < shelf[hole - 1].size:
            hole = hole - 1
        shelf.insert(hole, shelf.pop(i))
    return

def ssort(shelf):
    length = len(shelf)
    for j in range(0, length - 1):
        imin = j
        for i in range(j + 1, length):
            if shelf[i].size < shelf[imin].size:
                imin = i
        if imin != j:
            shelf.insert(j, shelf.pop(imin))

def partition(shelf, left, right, pivot_index):
    pivot = shelf[pivot_index]
    shelf.insert(right, shelf.pop(pivot_index))
    store_index = left
    for i in range(left, right): # range is non-inclusive of ending value
        if shelf[i].size < pivot.size:
            shelf.insert(store_index, shelf.pop(i))
            store_index = store_index + 1
    shelf.insert(store_index, shelf.pop(right)) # move pivot to correct position
    return store_index

def qsort(shelf, left, right):
    if left < right:
        pivot_index = left
        pivot_new_index = partition(shelf, left, right, pivot_index)
        qsort(shelf, left, pivot_new_index - 1)
        qsort(shelf, pivot_new_index + 1, right)

def randomize():
    disable_keys()
    clear()
    target = list(range(10))
    random.shuffle(target)
    for i, t in enumerate(target):
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()
#Display the word instructions to players
def show_text(text, line=0):
    line = 20 * line
    goto(0,-250 - line)
    write(text, align="center", font=("Newtimesroman", 20, ))

def start_ssort():
    disable_keys()
    clear()
    show_text("Selection Sort")
    ssort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_isort():
    disable_keys()
    clear()
    show_text("Insertion Sort")
    isort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_qsort():
    disable_keys()
    clear()
    show_text("Quicksort")
    qsort(s, 0, len(s) - 1)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def init_shelf():
    global s
    s = Shelf(-200)
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))

def disable_keys():
    onkey(None, "s")
    onkey(None, "i")
    onkey(None, "q")
    onkey(None, "r")

def enable_keys():
    onkey(start_isort, "i")
    onkey(start_ssort, "s")
    onkey(start_qsort, "q")
    onkey(randomize, "r")
    onkey(bye, "space")
#Basics function preparing
def main():
    getscreen().clearscreen()
    ht(); penup()
    init_shelf()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()
    listen()
    return "EVENTLOOP"

instructions1 = "Press i for insertion sort, s for selection sort, "
instructions2 = "q for quicksort, spacebar to quit, r to randomize"
#Start the program
if __name__=="__main__":
    msg = main()
    mainloop()
    
    
    
    
    
#pygame tommy
print ("WE PLAY A SONG , YOU GUESS EACH NOTE")
PLAY 
"""