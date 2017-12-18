#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:04:23 2017

@author: hailankan
"""
from tkinter import *
import sys


def shelf(self):
    self._31 = Button(filewin, image="blue.png", command=self.display)
    self._31.grid(row=4,column=0)
    self._32 = Button(filewin, image="...", command=self.display)
    self._32.grid(row=4,column=1)
    self._33 = Button(filewin, image="...", command=self.display)
    self._33.grid(row=4,column=2)
    self._34 = Button(filewin, image="...", command=self.display)
    self._34.grid(row=4,column=3)
    self._41 = Button(filewin, image="...", command=self.display)
    self._41.grid(row=6,column=0)
    self._42 = Button(filewin, image="...", command=self.display)
    self._42.grid(row=6,column=1)
    self._43 = Button(filewin, image="...", command=self.display)
    self._43.grid(row=6,column=2)
    self._44 = Button(filewin, image="...", command=self.display)
    self._44.grid(row=6,column=3)
        
        
        
        
def display():
    Photo = PhotoImage(file = "blue.png")
    f_Label = Label(root, image = Photo)
    f_Label.img = Photo
    f_Label.pack()