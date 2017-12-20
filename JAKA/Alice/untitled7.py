#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:00:00 2017
@author: haichunkan
a small eco system simulation
"""
import tkinter
'''
create classes that can store information
for animals: species, amount,prey, predator, reproduce rate, hunting successful rate
plants: name for the plant, amount, growing rate, its predator
'''

class eco():
    def __init__(self,species):
        self.species=""
class animals(eco):
    def __init__(self,species,prey,predator,amount,r_r,h_s_r):
        eco.__init__(self,species)
        self.prey= []
        self.predator= []
        self.amount=0
        self.r_r= 0
        self.h_s_r= 0
class plants(eco):
    def __init__(self,species,grow,amount,grasseater):
        eco.__init__(self,species)
        self.grow= 0
        self.grasseater= []
        self.amount= 0 
A=plants("A",0,0,[])
B=plants("B",0,0,[])
C=animals("C",[],[],0,0,0)
D=animals("D",[],[],0,0,0)
E=animals("E",[],[],0,0,0)
F=animals("F",[],[],0,0,0)        
# the window for setting information of  Plant A
def New_window_A():
        
        
        def nwA_quit():#close the window
            nwA.destroy()
        nwA=tkinter.Toplevel()
        # let the user input name
        tkinter.Label(nwA,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwA,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        #user can set the amount
        tkinter.Label(nwA,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwA,bd=5,textvariable=tkinter.IntVar(value=0))
        am.grid(row=1,column=1)
        #choose prey # disabled in A, since A has no prey
        tkinter.Label(nwA,text="prey:",state="disabled").grid(row=2,column=0)
        py=tkinter.Menubutton(nwA,text="choose:",state="disabled")
        py.grid(row=2,column=1)
        #choose predator, add the information into its list
        tkinter.Label(nwA,text="predator:").grid(row=3,column=0)
        
        tkinter.Label(nwA,text="predator:").grid(row=3,column=0)
        pr=tkinter.Menubutton(nwA,text="choose:")
        pr.grid(row=3,column=1)
        pr.menu = tkinter.Menu ( pr, tearoff = 0 ) 
        pr["menu"] = pr.menu 
        
        Item0 = tkinter.StringVar(value="") 
        Item1= tkinter.StringVar(value="") 
        Item2 = tkinter.StringVar(value="") 
        pr.menu.add_checkbutton ( label="Herbivore C", variable=Item0,onvalue="C",offvalue="") 
        pr.menu.add_checkbutton ( label="Herbivore D", variable=Item1,onvalue="D",offvalue="") 
        pr.menu.add_checkbutton ( label="Omnivore E", variable=Item2,onvalue="E",offvalue="")
       
        #set growing rate
        tkinter.Label(nwA,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nwA,from_=90,to=110)
        rr.grid(row=4,column=1)
        #set hunting successful rate # not available in A, as A does not hunt
        tkinter.Label(nwA,text="hunting successful rate:",state="disabled").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwA,from_=0,to=100,state="disabled")
        hsr.grid(row=5,column=1)
        def nwA_get():# if click on the button, information will be updated
            
            #A=plants("A",0,0,[])
            A.species=sp.get()
            A.amount=am.get()
            A.grow=rr.get()
            if Item0.get()=="C":
                A.grasseater.append(Item0.get())
            if Item1.get()=="D":
                A.grasseater.append(Item1.get())
            if Item2.get()=="E":
                A.grasseater.append(Item2.get())
            print(A.species,"amount:",A.amount,"growing rate:",A.grow,"grass eater:",A.grasseater)
            
        tkinter.Button(nwA,text="Set/Update",command=nwA_get).grid(row=6,column=1)
        tkinter.Button(nwA,text="Cancel",command=nwA_quit).grid(row=6,column=0)
       
        nwA.mainloop()
        
            
#window for B           
def New_window_B():# function similar to A
        
        def nwB_get():
            
            #B=plants("B",0,0,[])
            B.species=sp.get()
            B.amount=am.get()
            B.grow=rr.get()
            if Item3.get()=="C":
                B.grasseater.append(Item3.get())
            if Item4.get()=="D":
                B.grasseater.append(Item4.get())
            if Item5.get()=="E":
                B.grasseater.append(Item5.get())
            print(B.species,"amount:",B.amount,"growing rate:",B.grow,"grass eater:",B.grasseater)
        def nwB_quit():
            nwB.destroy()
        nwB=tkinter.Toplevel()
        tkinter.Label(nwB,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwB,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nwB,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwB,bd=5,textvariable=tkinter.IntVar(value=0))
        am.grid(row=1,column=1)
        
        tkinter.Label(nwB,text="prey:",state="disabled").grid(row=2,column=0)
        py=tkinter.Menubutton(nwB,text="choose:",state="disabled")
        py.grid(row=2,column=1)
        tkinter.Label(nwB,text="predator:").grid(row=3,column=0)
        pr=tkinter.Menubutton(nwB,text="choose:")
        pr.grid(row=3,column=1)
        pr.menu = tkinter.Menu ( pr, tearoff = 0 ) 
        pr["menu"] = pr.menu 
        Item3 = tkinter.StringVar() 
        Item4= tkinter.StringVar() 
        Item5 = tkinter.StringVar() 
        pr.menu.add_checkbutton ( label="Herbivore C", variable=Item3,onvalue="C") 
        pr.menu.add_checkbutton ( label="Herbivore D", variable=Item4,onvalue="D") 
        pr.menu.add_checkbutton ( label="Omnivore E", variable=Item5,onvalue="E")
        tkinter.Label(nwB,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nwB,from_=90,to=110)
        rr.grid(row=4,column=1)
        tkinter.Label(nwB,text="hunting successful rate:",state="disabled").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwB,from_=0,to=100,state="disabled")
        hsr.grid(row=5,column=1)
        tkinter.Button(nwB,text="Set/Update",command=nwB_get).grid(row=6,column=1)
        tkinter.Button(nwB,text="Cancel",command=nwB_quit).grid(row=6,column=0)
       
        nwB.mainloop()
#window for C
def New_window_C():
        
        def nwC_get():#update information
            #C=animals("C",[],[],0,0,0)
            C.species=sp.get()
            C.amount=am.get()
            if Item6.get()=="A":
                C.prey.append(Item6.get())
            if Item7.get()=="B":
                C.prey.append(Item7.get())
            if Item8.get()=="E":
                C.predator.append(Item8.get())
            if Item9.get()=="F":
                C.predator.append(Item9.get())
            C.r_r=rr.get()
            C.h_s_r=hsr.get()
            print(C.species,": amount:",C.amount,"reproduce rate:",C.r_r,"prey:",C.prey,"hunting successful rate",C.h_s_r,"predator:",C.predator)
        def nwC_quit():
            nwC.destroy()
        nwC=tkinter.Toplevel()
        tkinter.Label(nwC,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        #set the labels
        sp=tkinter.Entry(nwC,bd=5,textvariable=content)# where to set the name
        sp.grid(row=0,column=1)
        
        tkinter.Label(nwC,text="amount:").grid(row=1,column=0)
        #place to set the amount
        am=tkinter.Entry(nwC,bd=5,textvariable=tkinter.IntVar(value=0))
        am.grid(row=1,column=1)
        #choose the prey,A and/or B
        tkinter.Label(nwC,text="prey:").grid(row=2,column=0)
        py=tkinter.Menubutton(nwC,text="choose:")
        py.grid(row=2,column=1)
        py.menu = tkinter.Menu ( py, tearoff = 0 ) 
        py["menu"] = py.menu 
        Item6 = tkinter.StringVar() 
        Item7 = tkinter.StringVar() 
        py.menu.add_checkbutton ( label="Plant A", variable=Item6,onvalue="A") 
        py.menu.add_checkbutton ( label="Plant B", variable=Item7,onvalue="B") 
        #choose the predator,E and/or F
        tkinter.Label(nwC,text="predator:").grid(row=3,column=0)
        pr=tkinter.Menubutton(nwC,text="choose:")
        pr.grid(row=3,column=1)
        pr.menu = tkinter.Menu ( pr, tearoff = 0 ) 
        pr["menu"] = pr.menu 
        Item8 = tkinter.StringVar() 
        Item9 = tkinter.StringVar() 
        pr.menu.add_checkbutton ( label="Omnivore E", variable=Item8,onvalue="E") 
        pr.menu.add_checkbutton ( label="Carnivore F", variable=Item9,onvalue="F") 
        # set reproduce rate,from 90 to 110
        tkinter.Label(nwC,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nwC,from_=90,to=110)
        rr.grid(row=4,column=1)
        # the amount of plants to be eaten everyday
        tkinter.Label(nwC,text="hunting successful rate:").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwC,from_=1000,to=2000)
        hsr.grid(row=5,column=1)
        tkinter.Button(nwC,text="Set/Update",command=nwC_get).grid(row=6,column=1)
        tkinter.Button(nwC,text="Cancel",command=nwC_quit).grid(row=6,column=0)
       
        nwC.mainloop()
#window for D
def New_window_D():# function similar to C
        
        def nwD_get():
            #D=animals("D",[],[],0,0,0)
            D.species=sp.get()
            D.amount=am.get()
            if Item10.get()=="A":
                D.prey.append(Item10.get())
            if Item11.get()=="B":
                D.prey.append(Item11.get())
            if Item12.get()=="E":
                D.predator.append(Item12.get())
            if Item13.get()=="F":
                D.predator.append(Item13.get())
            D.r_r=rr.get()
            D.h_s_r=hsr.get()
            print(D.species,": amount:",D.amount,"reproduce rate:",D.r_r,"prey:",D.prey,"hunting successful rate",D.h_s_r,"predator:",D.predator)
        def nwD_quit():
            nwD.destroy()
        nwD=tkinter.Toplevel()
        tkinter.Label(nwD,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwD,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nwD,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwD,bd=5,textvariable=tkinter.IntVar(value=0))
        am.grid(row=1,column=1)
        
        tkinter.Label(nwD,text="prey:").grid(row=2,column=0)
        py=tkinter.Menubutton(nwD,text="choose:")
        py.grid(row=2,column=1)
        py.menu = tkinter.Menu ( py, tearoff = 0 ) 
        py["menu"] = py.menu 
        Item10 = tkinter.StringVar() 
        Item11 = tkinter.StringVar() 
        py.menu.add_checkbutton ( label="Plant A", variable=Item10,onvalue="A") 
        py.menu.add_checkbutton ( label="Plant B", variable=Item11,onvalue="B") 
        
        tkinter.Label(nwD,text="predator:").grid(row=3,column=0)
        pr=tkinter.Menubutton(nwD,text="choose:")
        pr.grid(row=3,column=1)
        pr.menu = tkinter.Menu ( pr, tearoff = 0 ) 
        pr["menu"] = pr.menu 
        Item12 = tkinter.StringVar() 
        Item13= tkinter.StringVar() 
        pr.menu.add_checkbutton ( label="Omnivore E", variable=Item12,onvalue="E") 
        pr.menu.add_checkbutton ( label="Carnivore F", variable=Item13,onvalue="F") 
        
        tkinter.Label(nwD,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nwD,from_=90,to=110)
        rr.grid(row=4,column=1)
        tkinter.Label(nwD,text="hunting successful rate:").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwD,from_=1000,to=2000)
        hsr.grid(row=5,column=1)
        tkinter.Button(nwD,text="Set/Update",command=nwD_get).grid(row=6,column=1)
        tkinter.Button(nwD,text="Cancel",command=nwD_quit).grid(row=6,column=0)
       
        nwD.mainloop()
#window for E                                            
def New_window_E():

        def nwE_quit():
            nwE.destroy()
        nwE=tkinter.Toplevel()
        tkinter.Label(nwE,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwE,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nwE,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwE,bd=5,textvariable=tkinter.IntVar(value=0))
        am.grid(row=1,column=1)
        # E has 4 choices of preys
        tkinter.Label(nwE,text="prey:").grid(row=2,column=0)
        py=tkinter.Menubutton(nwE,text="choose:")
        py.grid(row=2,column=1)
        py.menu = tkinter.Menu ( py, tearoff = 0 ) 
        py["menu"] = py.menu 
        Item14 = tkinter.StringVar() 
        Item15= tkinter.StringVar() 
        Item16= tkinter.StringVar()
        Item17=tkinter.StringVar()
        py.menu.add_checkbutton ( label="Plant A", variable=Item14,onvalue="A")
        py.menu.add_checkbutton ( label="Plant B", variable=Item15,onvalue="B")
        py.menu.add_checkbutton ( label="Herbivore C", variable=Item16,onvalue="C")
       
        py.menu.add_checkbutton ( label="Herbivore D", variable=Item17,onvalue="D") 
        
        tkinter.Label(nwE,text="predator:").grid(row=3,column=0)
        pr=tkinter.Menubutton(nwE,text="choose:")
        pr.grid(row=3,column=1)
        pr.menu = tkinter.Menu ( pr, tearoff = 0 ) 
        pr["menu"] = pr.menu 
        Item18 = tkinter.StringVar() 
        # E has only one predator 
        pr.menu.add_checkbutton ( label="carnivore F", variable=Item18,onvalue="F")
        tkinter.Label(nwE,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nwE,from_=90,to=110)
        rr.grid(row=4,column=1)
        tkinter.Label(nwE,text="hunting successful rate:").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwE,from_=100,to=1000)
        hsr.grid(row=5,column=1)
        def nwE_get():#update information
            
  
            #E=animals("E",[],[],0,0,0)
            E.species=sp.get()
            E.amount=am.get()
            if Item14.get()=="A":
                E.prey.append(Item14.get())
            if Item15.get()=="B":
                E.prey.append(Item15.get())
            if Item16.get()=="C":
                E.prey.append(Item16.get())
            if Item17.get()=="D":
                E.prey.append(Item17.get())
            if Item18.get()=="F":
                E.predator.append(Item18.get())
            E.r_r=rr.get()
            E.h_s_r=hsr.get()
            print(E.species,": amount:",E.amount,"reproduce rate:",E.r_r,"prey:",E.prey,"hunting successful rate",E.h_s_r,"predator:",E.predator)
        tkinter.Button(nwE,text="Set/Update",command=nwE_get).grid(row=6,column=1)
        tkinter.Button(nwE,text="Cancel",command=nwE_quit).grid(row=6,column=0)
       
        nwE.mainloop() 
#window for F            
def New_window_F():# F is the top predator
        
            
        def nwF_quit():
            nw.destroy()
        nw=tkinter.Toplevel()
        tkinter.Label(nw,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nw,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nw,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nw,bd=5,textvariable=tkinter.IntVar(value=0))
        am.grid(row=1,column=1)
        # F is a meat eater, so it has 3 prey choices
        tkinter.Label(nw,text="prey:").grid(row=2,column=0)
        py=tkinter.Menubutton(nw,text="choose:")
        py.grid(row=2,column=1)
        py.menu = tkinter.Menu ( py, tearoff = 0 ) 
        py["menu"] = py.menu 
        Item19 = tkinter.StringVar() 
        Item20= tkinter.StringVar() 
        Item21= tkinter.StringVar()
        py.menu.add_checkbutton ( label="Herbivore C", variable=Item19,onvalue="C") 
        py.menu.add_checkbutton ( label="Herbivore D", variable=Item20,onvalue="D") 
        py.menu.add_checkbutton ( label="Omnivore E", variable=Item21,onvalue="E")
        #predator choice not available in F, F is the top predator
        tkinter.Label(nw,text="predator:",state="disabled").grid(row=3,column=0)
        pr=tkinter.Menubutton(nw,text="choose:",state="disabled")
        pr.grid(row=3,column=1)
        
        tkinter.Label(nw,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nw,from_=90,to=110)
        rr.grid(row=4,column=1)
        #its hunting successful rate should be low to keep the system running
        # % to catch a predator: 0-50%
        tkinter.Label(nw,text="hunting successful rate:").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nw,from_=0,to=50)
        hsr.grid(row=5,column=1)
        def nwF_get():
            #F=animals("F",[],[],0,0,0)
            F.species=sp.get()
            F.amount=am.get()
            if Item19.get()=="C":
                F.prey.append(Item19.get())
            if Item20.get()=="D":
                F.prey.append(Item20.get())
            if Item21.get()=="E":
                F.prey.append(Item21.get())
            F.r_r=rr.get()
            F.h_s_r=hsr.get()
            print(F.species,": amount:",F.amount,"reproduce rate:",F.r_r,"prey:",F.prey,"hunting successful rate",F.h_s_r,"predator:",F.predator)
        tkinter.Button(nw,text="Set/Update",command=nwF_get).grid(row=6,column=1)
        tkinter.Button(nw,text="Cancel",command=nwF_quit).grid(row=6,column=0)
       
        nw.mainloop()
        
    
        

print ("Set the information for each species")
# set the parent window
pw=tkinter.Tk()

pw.resizable(False,False)

#labels, from A to F
title_label = tkinter.Label(pw,text="Ecosystem Simulation", bg="white").grid(row=0,column=0,columnspan=3)
tkinter.Label(pw,text="Carnivore F", bg="white").grid(row=4,column=0,columnspan=2)
tkinter.Label(pw,text="Omnivore E",bg="white").grid(row=6,column=0,columnspan=2)
tkinter.Label(pw,text="Herbivore C", bg="white").grid(row=8,column=0)
tkinter.Label(pw,text="Herbivore D", bg="white").grid(row=8,column=1)
tkinter.Label(pw,text="Plant A", bg="white").grid(row=10,column=0)
tkinter.Label(pw,text="Plant B",bg="white").grid(row=10,column=1)
#buttons, will open new windows
bt1=tkinter.Button(pw,text="Carnivore F", bg="white",width=10,height=5,command=New_window_F).grid(row=3,column=0,columnspan=2)
bt2=tkinter.Button(pw,text="Omnivore E",bg="white",width=10,height=5,command=New_window_E).grid(row=5,column=0,columnspan=2)
bt3=tkinter.Button(pw,text="Herbivore C", bg="white",width=10,height=5,command=New_window_C)
bt3.grid(row=7,column=0)
bt4=tkinter.Button(pw,text="Herbivore D", bg="white",width=10,height=5,command=New_window_D).grid(row=7,column=1)
bt5=tkinter.Button(pw,text="Plant A", bg="white",width=10,height=5,command=New_window_A).grid(row=9,column=0)
bt6=tkinter.Button(pw,text="Plant B",bg="white",width=10,height=5,command=New_window_B).grid(row=9,column=1)

pw.mainloop()

print("Set the turns to run")  
time=input("times:")#set running times
#set amount of animals to be eaten by each animal
l=[int(A.amount),int(B.amount),int(C.amount)*int(C.h_s_r),int(D.amount)*int(D.h_s_r),int(E.amount)*int(E.h_s_r),int(F.amount)*int(F.h_s_r)]
print("initial amount",l)
d=["A","B","C","D","E","F"]
# set the original amount that has been eaten
totalA=0
totalB=0
totalC=0
totalD=0
totalE=0
#calculate the amount has been eaten by each of its predators
#calculate the amount left after reproduce and hunting every time
for i in range (0,int(time)):
    print("time",i+1,":")
    for ii in range(0,len(A.grasseater)):
        x=d.index(A.grasseater[ii])
        totalA+=l[x]
    A.amount=int(A.grow)*int(A.amount)/100-totalA
    print("A:",A.amount)
    for ii in range(0,len(B.grasseater)):
        x=d.index(B.grasseater[ii])
        totalB+=l[x]
    B.amount=int(B.grow)*int(B.amount)/100-totalB
    print("B:",B.amount)
    for ii in range(0,len(C.predator)):
        x=d.index(C.predator[ii])
        totalC+=l[x]
    C.amount=int(C.r_r)*int(C.amount)/100-totalC
    print("C:",C.amount)
    for ii in range(0,len(D.predator)):
        x=d.index(D.predator[ii])
        totalD+=l[x]
    D.amount=int(D.r_r)*int(D.amount)/100-totalD
    print("D:",D.amount)
    for ii in range(0,len(E.predator)):
        x=d.index(E.predator[ii])
        totalE+=l[x]
    E.amount=int(E.amount)*int(E.r_r)/100-totalE
    print("E:",E.amount)
    
    F.amount=int(F.amount)*int(F.r_r)/100
    print("F:",F.amount)     
#print the result each time 
if A.amount<0 or B.amount<0 or C.amount<0 or D.amount<0 or E.amount<0 or F.amount<0:
    print("Failed!")
else:
    print("Successful!")    