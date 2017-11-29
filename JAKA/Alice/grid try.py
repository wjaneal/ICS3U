#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:15:11 2017

@author: haichunkan
"""
import tkinter
def New_window():
    nw=tkinter.Toplevel()
    tkinter.Label(nw,text="species:").grid(row=0,column=0)
    tkinter.Entry(nw,bd=5,textvariable=tkinter.StringVar(value="")).grid(row=0,column=1)
    tkinter.Label(nw,text="amount:").grid(row=1,column=0)
    tkinter.Entry(nw,bd=5,textvariable=tkinter.StringVar(value="")).grid(row=1,column=1)
    tkinter.Label(nw,text="prey:").grid(row=2,column=0)
    tkinter.Label(nw,text="predator:").grid(row=3,column=0)
    tkinter.Label(nw,text="reproduce rate:").grid(row=4,column=0)
    tkinter.Spinbox(nw,from_=0,to=100).grid(row=4,column=1)
    tkinter.Label(nw,text="hunting successful rate:").grid(row=5,column=0)
    tkinter.Spinbox(nw,from_=0,to=100).grid(row=5,column=1)
    tkinter.Button(nw,text="Cancel").grid(row=6,column=0)
    tkinter.Button(nw,text="Set/Update").grid(row=6,column=1)
pw=tkinter.Tk()

pw.resizable(False,False)
#root.geometry("50*50")


title_label = tkinter.Label(pw,text="Ecosystem Simulation", bg="white").grid(row=0,column=0,columnspan=3)
tkinter.Label(pw,text="Top Predator K", bg="white").grid(row=2,column=0,columnspan=3)
tkinter.Label(pw,text="Carnivore I", bg="white").grid(row=4,column=0,columnspan=2)
tkinter.Label(pw,text="Carnivore J", bg="white").grid(row=4,column=1,columnspan=2)
tkinter.Label(pw,text="Omnivore G",bg="white").grid(row=6,column=0,columnspan=2)
tkinter.Label(pw,text="Omnivore H", bg="white").grid(row=6,column=1,columnspan=2)
tkinter.Label(pw,text="Herbivore D", bg="white").grid(row=8,column=0)
tkinter.Label(pw,text="Herbivore E", bg="white").grid(row=8,column=1)
tkinter.Label(pw,text="Herbivore F", bg="white").grid(row=8,column=2)
tkinter.Label(pw,text="Plant A", bg="white").grid(row=10,column=0)
tkinter.Label(pw,text="Plant B",bg="white").grid(row=10,column=1)
tkinter.Label(pw,text="Plant C", bg="white").grid(row=10,column=2)

tkinter.Button(pw,text="Top Predator K", bg="white",width=10,height=5,command=New_window).grid(row=1,column=0,columnspan=3)
tkinter.Button(pw,text="Carnivore I", bg="white",width=10,height=5).grid(row=3,column=0,columnspan=2)
tkinter.Button(pw,text="Carnivore J", bg="white",width=10,height=5).grid(row=3,column=1,columnspan=2)
tkinter.Button(pw,text="Omnivore G",bg="white",width=10,height=5).grid(row=5,column=0,columnspan=2)
tkinter.Button(pw,text="Omnivore H", bg="white",width=10,height=5).grid(row=5,column=1,columnspan=2)
tkinter.Button(pw,text="Herbivore D", bg="white",width=10,height=5).grid(row=7,column=0)
tkinter.Button(pw,text="Herbivore E", bg="white",width=10,height=5).grid(row=7,column=1)
tkinter.Button(pw,text="Herbivore F", bg="white",width=10,height=5).grid(row=7,column=2)
tkinter.Button(pw,text="Plant A", bg="white",width=10,height=5).grid(row=9,column=0)
tkinter.Button(pw,text="Plant B",bg="white",width=10,height=5).grid(row=9,column=1)
tkinter.Button(pw,text="Plant C", bg="white",width=10,height=5).grid(row=9,column=2)    



pw.mainloop()


