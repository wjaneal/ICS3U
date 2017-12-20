#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:45:30 2017
final project 
@author: haichunkan
"""
import tkinter

def hit_me():
    global on_hit
    if on_hit==0:
        on_hit=1
        var.set("T")
    elif on_hit==1:
        on_hit=2
        var.set("F")
    elif on_hit==2:
        on_hit=0
        var.set("")
    
filewin=tkinter.Tk()
var=tkinter.StringVar()
tkinter.Label(filewin,text="a").grid(row=0,column=0)
tkinter.Label(filewin,text="b").grid(row=0,column=1)
tkinter.Label(filewin).grid(row=0,column=2)
tkinter.Label(filewin).grid(row=0,column=3)
tkinter.Label(filewin).grid(row=1,column=0)
tkinter.Label(filewin).grid(row=1,column=1)
tkinter.Label(filewin).grid(row=1,column=2)
tkinter.Label(filewin).grid(row=1,column=3)
tkinter.Button(filewin,bg="black",text="button",command=hit_me).grid(row=2,column=2)
tkinter.Label(filewin,textvariable=var,bg="yellow").grid(row=3,column=2)
on_hit=0
filewin.mainloop()
       