#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:29:32 2017

@author: chenquancheng
"""

from tkinter import *
import sys
from tkinter import font
import math
from random import shuffle

class MenuBar(Menu):
    def destroywin(self):
        self.filewin2.destroy()
    
    def start(self):
        self.filewin2 = Toplevel(self)
        self.instructions = Label(self.filewin2,text="Please select three cases you want to open.",bg="lightgreen").grid(row=0,column=0)
        self.okbutton = Button(self.filewin2,text="OK",bg="lightgreen",command=self.destroywin).grid(row=1,column=0)
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        filewin = Toplevel(self)
        self.Cases=[1,2,5,10,100,250,500,750,1000,2500,5000,10000,25000,50000,100000,200000,250000,500000,750000,1000000,2000000,2500000,5000000,7500000,10000000]
        shuffle(self.Cases)
        self.money=[]
        self.offer=0
        self.sum=0
        for i in range(0,len(self.Cases)):
            self.money.append(self.Cases[i])
            self.sum+=self.Cases[i]
        self.offer=self.sum/len(self.Cases)
        self.Button1 = Button(filewin,text="Case 1",bg="lightgreen",command=lambda:self.open_case(self.Button1,self.money[0]))
        self.Button1.grid(row=0,column=0)
        self.Button2 = Button(filewin,text="Case 2",bg="lightgreen",command=lambda:self.open_case(self.Button2,self.money[1]))
        self.Button2.grid(row=0,column=1)
        self.Button3 = Button(filewin,text="Case 3",bg="lightgreen",command=lambda:self.open_case(self.Button3,self.money[2]))
        self.Button3.grid(row=0,column=2)
        self.Button4 = Button(filewin,text="Case 4",bg="lightgreen",command=lambda:self.open_case(self.Button4,self.money[3]))
        self.Button4.grid(row=0,column=3)
        self.Button5 = Button(filewin,text="Case 5",bg="lightgreen",command=lambda:self.open_case(self.Button5,self.money[4]))
        self.Button5.grid(row=0,column=4)
        self.Button6 = Button(filewin,text="Case 6",bg="lightgreen",command=lambda:self.open_case(self.Button6,self.money[5]))
        self.Button6.grid(row=1,column=0)
        self.Button7 = Button(filewin,text="Case 7",bg="lightgreen",command=lambda:self.open_case(self.Button7,self.money[6]))
        self.Button7.grid(row=1,column=1)
        self.Button8 = Button(filewin,text="Case 8",bg="lightgreen",command=lambda:self.open_case(self.Button8,self.money[7]))
        self.Button8.grid(row=1,column=2)
        self.Button9 = Button(filewin,text="Case 9",bg="lightgreen",command=lambda:self.open_case(self.Button9,self.money[8]))
        self.Button9.grid(row=1,column=3)
        self.Button10 = Button(filewin,text="Case 10",bg="lightgreen",command=lambda:self.open_case(self.Button10,self.money[9]))
        self.Button10.grid(row=1,column=4)
        self.Button11 = Button(filewin,text="Case 11",bg="lightgreen",command=lambda:self.open_case(self.Button11,self.money[10]))
        self.Button11.grid(row=2,column=0)
        self.Button12 = Button(filewin,text="Case 12",bg="lightgreen",command=lambda:self.open_case(self.Button12,self.money[11]))
        self.Button12.grid(row=2,column=1)
        self.Button13 = Button(filewin,text="Case 13",bg="lightgreen",command=lambda:self.open_case(self.Button13,self.money[12]))
        self.Button13.grid(row=2,column=2)
        self.Button14 = Button(filewin,text="Case 14",bg="lightgreen",command=lambda:self.open_case(self.Button14,self.money[13]))
        self.Button14.grid(row=2,column=3)
        self.Button15 = Button(filewin,text="Case 15",bg="lightgreen",command=lambda:self.open_case(self.Button15,self.money[14]))
        self.Button15.grid(row=2,column=4)
        self.Button16 = Button(filewin,text="Case 16",bg="lightgreen",command=lambda:self.open_case(self.Button16,self.money[15]))
        self.Button16.grid(row=3,column=0)
        self.Button17 = Button(filewin,text="Case 17",bg="lightgreen",command=lambda:self.open_case(self.Button17,self.money[16]))
        self.Button17.grid(row=3,column=1)
        self.Button18 = Button(filewin,text="Case 18",bg="lightgreen",command=lambda:self.open_case(self.Button18,self.money[17]))
        self.Button18.grid(row=3,column=2)
        self.Button19 = Button(filewin,text="Case 19",bg="lightgreen",command=lambda:self.open_case(self.Button19,self.money[18]))
        self.Button19.grid(row=3,column=3)
        self.Button20 = Button(filewin,text="Case 20",bg="lightgreen",command=lambda:self.open_case(self.Button20,self.money[19]))
        self.Button20.grid(row=3,column=4)
        self.Button21 = Button(filewin,text="Case 21",bg="lightgreen",command=lambda:self.open_case(self.Button21,self.money[20]))
        self.Button21.grid(row=4,column=0)
        self.Button22 = Button(filewin,text="Case 22",bg="lightgreen",command=lambda:self.open_case(self.Button22,self.money[21]))
        self.Button22.grid(row=4,column=1)
        self.Button23 = Button(filewin,text="Case 23",bg="lightgreen",command=lambda:self.open_case(self.Button23,self.money[22]))
        self.Button23.grid(row=4,column=2)
        self.Button24 = Button(filewin,text="Case 24",bg="lightgreen",command=lambda:self.open_case(self.Button24,self.money[23]))
        self.Button24.grid(row=4,column=3)
        self.Button25 = Button(filewin,text="Case 25",bg="lightgreen",command=lambda:self.open_case(self.Button25,self.money[24]))
        self.Button25.grid(row=4,column=4)
    
    def offers(self):
        self.filewin1 = Toplevel(self)
        self.offer1.set(int(self.offer))
        self.label1=Label(self.filewin1,text="Hi,this is the bank",bg="lightgreen").grid(row=0,column=0)
        self.label2=Label(self.filewin1,text="We would like to offer you an offer of $",bg="lightgreen").grid(row=1,column=0)
        self.offerlabel=Label(self.filewin1,textvariable=self.offer1).grid(row=1,column=1)
        self.label3=Label(self.filewin1,text="Would you like to accept the offer?",bg="lightgreen").grid(row=2,column=0)
        self.yesbutton=Button(self.filewin1,text="Yes",command=self.donothing)
        self.yesbutton.grid(row=3,column=0)
        self.nobutton=Button(self.filewin1,text="No",command=self.no)
        self.nobutton.grid(row=3,column=1)
    
    def open_case(self,cButton,n):
        cButton.grid_remove()
        self.Cases.remove(n)
        for i in range(0,len(self.Cases)):
            self.sum+=self.Cases[i]
        self.offer=self.sum/len(self.Cases)
        if((25-len(self.Cases))%3==0 and len(self.Cases)!=25):
            self.offers()
    
    def no(self):
        self.filewin1.destroy()
        
    def donothing(self):
        pass
    
    
    def __init__(self, parent):
        Menu.__init__(self, parent)
        self.offer1 = StringVar()
        filemenu = Menu(self, tearoff=0) 
        filemenu.add_command(label="Start", command=self.start) 
        filemenu.add_command(label="Exit", command=self.quit)
        self.add_cascade(label="Game", menu=filemenu)
        self.welcome=Label(parent,text="Welcome to 'The Banker's Case!",bg="lightgreen").grid(row=0,column=0)
        self.namelabel=Label(parent,text="What's your name?",bg="lightgreen").grid(row=1,column=0)
        self.name=Entry(parent,bd=5,textvariable=StringVar(value="0")).grid(row=1,column=1)
        self.sbutton=Button(parent,text="Start",command=self.start).grid(row=2,column=0)
    def quit(self):
        app.destroy()
          
#Main class - calls menubar class
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)


#Start the program:
if __name__ == "__main__":
    app=App()
    app.title("The Banker's Case")
    app.mainloop()