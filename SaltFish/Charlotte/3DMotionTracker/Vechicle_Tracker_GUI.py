
# use namespace to avoid conflict with PIL's Image
import Tkinter as tk
from Tkinter import *
import math
import os

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Initiate Flight", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "Initiating Flight Sequence!"

root = Tk()

app = App(root)

root.mainloop()
