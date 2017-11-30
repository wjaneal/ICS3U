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

flag=0

class MenuBar(Menu):
    def destroywin(self,filewinc):
        filewinc.destroy()
    
    def start2(self):
        self.filewin3.destroy()
        self.filewin2 = Toplevel(self)
        self.instructions = Label(self.filewin2,text="Please select three cases you want to open.",bg="lightgreen").grid(row=0,column=0)
        self.okbutton = Button(self.filewin2,text="OK",bg="lightgreen",command=lambda:self.destroywin(self.filewin2)).grid(row=1,column=0)
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        filewin = Toplevel(self)
        self.Cases=[1,2,5,10,100,250,500,750,1000,2500,5000,10000,25000,50000,75000,100000,200000,250000,500000,750000,1000000,2000000,2500000,5000000,7500000,10000000]
        self.money=[]
        self.offer=0
        self.sum=0
        shuffle(self.Cases)
        for i in range(0,len(self.Cases)):
            self.money.append(self.Cases[i])
        self.Label26=[]
        for i in range(0,26):
            self.Label26.append(Label(filewin,text=self.Cases[25-i]))
            self.Label26[i].grid(row=7+int(i/5),column=(i%5))
        #self.Label1 = Label(filewin,text=self.Cases[0])
        #self.Label1.grid(row=6,column=0)
        self.Button1 = Button(filewin,text="Case 1",bg="lightgreen",command=lambda:self.open_case(self.Button1,self.money[0],self.Label26[25]))
        self.Button1.grid(row=0,column=0)
        self.Button2 = Button(filewin,text="Case 2",bg="lightgreen",command=lambda:self.open_case(self.Button2,self.money[1],self.Label26[24]))
        self.Button2.grid(row=0,column=1)
        self.Button3 = Button(filewin,text="Case 3",bg="lightgreen",command=lambda:self.open_case(self.Button3,self.money[2],self.Label26[23]))
        self.Button3.grid(row=0,column=2)
        self.Button4 = Button(filewin,text="Case 4",bg="lightgreen",command=lambda:self.open_case(self.Button4,self.money[3],self.Label26[22]))
        self.Button4.grid(row=0,column=3)
        self.Button5 = Button(filewin,text="Case 5",bg="lightgreen",command=lambda:self.open_case(self.Button5,self.money[4],self.Label26[21]))
        self.Button5.grid(row=0,column=4)
        self.Button6 = Button(filewin,text="Case 6",bg="lightgreen",command=lambda:self.open_case(self.Button6,self.money[5],self.Label26[20]))
        self.Button6.grid(row=1,column=0)
        self.Button7 = Button(filewin,text="Case 7",bg="lightgreen",command=lambda:self.open_case(self.Button7,self.money[6],self.Label26[19]))
        self.Button7.grid(row=1,column=1)
        self.Button8 = Button(filewin,text="Case 8",bg="lightgreen",command=lambda:self.open_case(self.Button8,self.money[7],self.Label26[18]))
        self.Button8.grid(row=1,column=2)
        self.Button9 = Button(filewin,text="Case 9",bg="lightgreen",command=lambda:self.open_case(self.Button9,self.money[8],self.Label26[17]))
        self.Button9.grid(row=1,column=3)
        self.Button10 = Button(filewin,text="Case 10",bg="lightgreen",command=lambda:self.open_case(self.Button10,self.money[9],self.Label26[16]))
        self.Button10.grid(row=1,column=4)
        self.Button11 = Button(filewin,text="Case 11",bg="lightgreen",command=lambda:self.open_case(self.Button11,self.money[10],self.Label26[15]))
        self.Button11.grid(row=2,column=0)
        self.Button12 = Button(filewin,text="Case 12",bg="lightgreen",command=lambda:self.open_case(self.Button12,self.money[11],self.Label26[14]))
        self.Button12.grid(row=2,column=1)
        self.Button13 = Button(filewin,text="Case 13",bg="lightgreen",command=lambda:self.open_case(self.Button13,self.money[12],self.Label26[13]))
        self.Button13.grid(row=2,column=2)
        self.Button14 = Button(filewin,text="Case 14",bg="lightgreen",command=lambda:self.open_case(self.Button14,self.money[13],self.Label26[12]))
        self.Button14.grid(row=2,column=3)
        self.Button15 = Button(filewin,text="Case 15",bg="lightgreen",command=lambda:self.open_case(self.Button15,self.money[14],self.Label26[11]))
        self.Button15.grid(row=2,column=4)
        self.Button16 = Button(filewin,text="Case 16",bg="lightgreen",command=lambda:self.open_case(self.Button16,self.money[15],self.Label26[10]))
        self.Button16.grid(row=3,column=0)
        self.Button17 = Button(filewin,text="Case 17",bg="lightgreen",command=lambda:self.open_case(self.Button17,self.money[16],self.Label26[9]))
        self.Button17.grid(row=3,column=1)
        self.Button18 = Button(filewin,text="Case 18",bg="lightgreen",command=lambda:self.open_case(self.Button18,self.money[17],self.Label26[8]))
        self.Button18.grid(row=3,column=2)
        self.Button19 = Button(filewin,text="Case 19",bg="lightgreen",command=lambda:self.open_case(self.Button19,self.money[18],self.Label26[7]))
        self.Button19.grid(row=3,column=3)
        self.Button20 = Button(filewin,text="Case 20",bg="lightgreen",command=lambda:self.open_case(self.Button20,self.money[19],self.Label26[6]))
        self.Button20.grid(row=3,column=4)
        self.Button21 = Button(filewin,text="Case 21",bg="lightgreen",command=lambda:self.open_case(self.Button21,self.money[20],self.Label26[5]))
        self.Button21.grid(row=4,column=0)
        self.Button22 = Button(filewin,text="Case 22",bg="lightgreen",command=lambda:self.open_case(self.Button22,self.money[21],self.Label26[4]))
        self.Button22.grid(row=4,column=1)
        self.Button23 = Button(filewin,text="Case 23",bg="lightgreen",command=lambda:self.open_case(self.Button23,self.money[22],self.Label26[3]))
        self.Button23.grid(row=4,column=2)
        self.Button24 = Button(filewin,text="Case 24",bg="lightgreen",command=lambda:self.open_case(self.Button24,self.money[23],self.Label26[2]))
        self.Button24.grid(row=4,column=3)
        self.Button25 = Button(filewin,text="Case 25",bg="lightgreen",command=lambda:self.open_case(self.Button25,self.money[24],self.Label26[1]))
        self.Button25.grid(row=4,column=4)
        self.Button26 = Button(filewin,text="Case 26",bg="lightgreen",command=lambda:self.open_case(self.Button26,self.money[25],self.Label26[0]))
        self.Button26.grid(row=5,column=0)
        self.remoneylabel = Label(filewin,text="Remaining money",bg="lightgreen").grid(row=6,column=0,columnspan=2)
            
    
    def offers(self):
        self.filewin1 = Toplevel(self)
        self.offer=0
        self.sum=0
        for i in range(0,len(self.Cases)):
            self.money.append(self.Cases[i])
            self.sum+=self.Cases[i]
        self.offer=self.sum/len(self.Cases)
        self.offer1.set(int(self.offer))
        self.label1=Label(self.filewin1,text="Hi,this is the bank",bg="lightgreen").grid(row=0,column=0)
        self.label2=Label(self.filewin1,text="We would like to offer you an offer of $",bg="lightgreen").grid(row=1,column=0)
        self.offerlabel=Label(self.filewin1,textvariable=self.offer1).grid(row=1,column=1)
        self.label3=Label(self.filewin1,text="Would you like to accept the offer?",bg="lightgreen").grid(row=2,column=0)
        self.yesbutton=Button(self.filewin1,text="Yes",command=self.end)
        self.yesbutton.grid(row=3,column=0)
        self.nobutton=Button(self.filewin1,text="No",command=self.no)
        self.nobutton.grid(row=3,column=1)
    
    def open_case(self,cButton,n,cLabel):
        global flag
        cButton.grid_remove()
        #cLabel.grid_remove()
        cLabel.grid_remove()
        self.Cases.remove(n)
        if(len(self.Cases)==1 and flag==0):
            self.end()
        elif((26-len(self.Cases))%3==0 and len(self.Cases)!=26 and len(self.Cases)>=2 and flag==0):
            self.offers()
        elif(len(self.Cases)==1 and flag==1):
            self.end()
        
    
    def no(self):
        if (len(self.Cases)>2):
            self.filewin1.destroy()
            self.filewin2=Toplevel(self)
            self.instructions = Label(self.filewin2,text="Please select three cases you want to open.",bg="lightgreen").grid(row=0,column=0)
            self.okbutton = Button(self.filewin2,text="OK",bg="lightgreen",command=lambda:self.destroywin(self.filewin2)).grid(row=1,column=0)
        elif(len(self.Cases)<=2):
            self.filewin1.destroy()
            self.filewin5=Toplevel(self)
            self.instructions = Label(self.filewin5,text="Please open one of the cases.",bg="lightgreen").grid(row=0,column=0)
            self.okbutton = Button(self.filewin5,text="OK",bg="lightgreen",command=lambda:self.destroywin(self.filewin5)).grid(row=1,column=0)
    
    def end(self):
        global flag
        self.filewin1.destroy()
        if (len(self.Cases)==1 and flag==0):
            self.filewin6=Toplevel(self)
            self.result=Label(self.filewin6,text="You get $",bg="lightgreen").grid(row=0,column=0)
            self.result2=Label(self.filewin6,text=self.Cases[0],bg="lightgreen").grid(row=0,column=1)
            if (self.offer<=self.Cases[0]):
                self.result3=Label(self.filewin6,text="Wise Choice!",bg="lightgreen").grid(row=1,column=0)
            else:
                self.result3=Label(self.filewin6,text="Bad Luck!",bg="lightgreen").grid(row=1,column=0)
        elif(len(self.Cases)!=1 and flag==0):
            self.filewin6=Toplevel(self)
            flag=1
            self.result5=Label(self.filewin6,text="You get $",bg="lightgreen").grid(row=0,column=0)
            self.result6=Label(self.filewin6,textvariable=self.offer1,bg="lightgreen").grid(row=0,column=1)
            self.instructions3=Label(self.filewin6,text="Now you can open the remaining cases to see whether you make a good choice.",bg="lightgreen").grid(row=1,column=0)
            self.okbutton2=Button(self.filewin6,text="OK",bg="lightgreen",command=lambda:self.destroywin(self.filewin6)).grid(row=2,column=0)
        elif(len(self.Cases)==1 and flag==1):
            self.filewin6=Toplevel(self)
            if (self.offer>=self.Cases[0]):
                self.result5=Label(self.filewin6,text="It seems that you have made a wise choice",bg="lightgreen").grid(row=0,column=0)
            else:
                self.instructions3=Label(self.filewin6,text="It seems that you are not lucky enough",bg="lightgreen").grid(row=0,column=0)
               
    def donothing(self):
        pass
    
    def __init__(self, parent):
        Menu.__init__(self, parent)
        self.offer1 = StringVar()
        filemenu = Menu(self, tearoff=0) 
        filemenu.add_command(label="Start", command=self.start) 
        filemenu.add_command(label="Exit", command=self.quit)
        self.canvas = Canvas(parent,width=1000,height=1000,bg="white")
        self.filename=PhotoImage(master=self.canvas, file="deal.gif")
        self.image1=self.canvas.create_image(500,300,image=self.filename)
        self.canvas.pack()

       
    
    def start(self):
        self.filewin3=Toplevel(self)
        self.welcome=Label(self.filewin3,text="Welcome to 'The Banker's Case'!",bg="lightgreen").grid(row=0,column=0)
        self.namelabel=Label(self.filewin3,text="What's your name?",bg="lightgreen").grid(row=1,column=0)
        self.name=Entry(self.filewin3,bd=5,textvariable=StringVar(value="0")).grid(row=1,column=1)
        self.sbutton=Button(self.filewin3,text="Start",command=self.start2).grid(row=2,column=0)
        
        

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