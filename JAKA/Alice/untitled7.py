#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:00:00 2017

@author: haichunkan
"""
import tkinter
#create a class that can store information
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
        
        
        def nwA_quit():
            nwA.destroy()
        nwA=tkinter.Toplevel()
        # let the user input name
        tkinter.Label(nwA,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwA,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        #user can input amount
        tkinter.Label(nwA,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwA,bd=5,textvariable=tkinter.StringVar(value=""))
        am.grid(row=1,column=1)
        #choose prey # disabled in A
        tkinter.Label(nwA,text="prey:",state="disabled").grid(row=2,column=0)
        py=tkinter.Menubutton(nwA,text="choose:",state="disabled")
        py.grid(row=2,column=1)
        #choose predator
        tkinter.Label(nwA,text="predator:").grid(row=3,column=0)
        Item0 = tkinter.StringVar() 
        Item1= tkinter.StringVar() 
        Item2 = tkinter.StringVar()
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
        #set hunting successful rate # not available in A
        tkinter.Label(nwA,text="hunting successful rate:",state="disabled").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwA,from_=0,to=100,state="disabled")
        hsr.grid(row=5,column=1)
        def nwA_get():
            
            A=plants("A",0,0,[])
            A.species=sp.get()
            A.amount=am.get()
            A.grow=rr.get()
            A.grasseater.append(Item0.get())
            A.grasseater.append(Item1.get())
            A.grasseater.append(Item2.get())
            print(A.species,A.amount,A.grow,A.grasseater)
            
        tkinter.Button(nwA,text="Set/Update",command=nwA_get).grid(row=6,column=1)
        tkinter.Button(nwA,text="Cancel",command=nwA_quit).grid(row=6,column=0)
       
        nwA.mainloop()
        
            
#window for B           
def New_window_B():
        
        def nwB_get():
            
            B=plants("B",0,0,[])
            B.species=sp.get()
            B.amount=am.get()
            B.grow=rr.get()
            B.grasseater.append(Item3.get())
            B.grasseater.append(Item4.get())
            B.grasseater.append(Item5.get())
            print(B.species,B.amount,B.grow,B.grasseater)
        def nwB_quit():
            nwB.destroy()
        nwB=tkinter.Toplevel()
        tkinter.Label(nwB,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwB,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nwB,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwB,bd=5,textvariable=tkinter.StringVar(value=""))
        am.grid(row=1,column=1)
        
        tkinter.Label(nwB,text="prey:").grid(row=2,column=0)
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
        rr=tkinter.Spinbox(nwB,from_=9,to=110)
        rr.grid(row=4,column=1)
        tkinter.Label(nwB,text="hunting successful rate:",state="disabled").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwB,from_=0,to=100)
        hsr.grid(row=5,column=1)
        tkinter.Button(nwB,text="Set/Update",command=nwB_get).grid(row=6,column=1)
        tkinter.Button(nwB,text="Cancel",command=nwB_quit).grid(row=6,column=0)
       
        nwB.mainloop()
#window for C
def New_window_C():
        
        def nwC_get():
            C=animals("C",[],[],0,0,0)
            C.species=sp.get()
            C.amount=am.get()
            C.prey.append(Item6.get())
            C.prey.append(Item7.get())
            C.predator.append(Item8.get())
            C.predator.append(Item9.get())
            C.r_r=rr.get()
            C.h_s_r=hsr.get()
            print(C.species,C.amount,C.r_r,C.prey,C.h_s_r,C.predator)
        def nwC_quit():
            nwC.destroy()
        nwC=tkinter.Toplevel()
        tkinter.Label(nwC,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwC,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nwC,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwC,bd=5,textvariable=tkinter.StringVar(value=""))
        am.grid(row=1,column=1)
        
        tkinter.Label(nwC,text="prey:").grid(row=2,column=0)
        py=tkinter.Menubutton(nwC,text="choose:")
        py.grid(row=2,column=1)
        py.menu = tkinter.Menu ( py, tearoff = 0 ) 
        py["menu"] = py.menu 
        Item6 = tkinter.StringVar() 
        Item7 = tkinter.StringVar() 
        py.menu.add_checkbutton ( label="Plant A", variable=Item6,onvalue="A") 
        py.menu.add_checkbutton ( label="Plant B", variable=Item7,onvalue="B") 
        
        tkinter.Label(nwC,text="predator:").grid(row=3,column=0)
        pr=tkinter.Menubutton(nwC,text="choose:")
        pr.grid(row=3,column=1)
        pr.menu = tkinter.Menu ( pr, tearoff = 0 ) 
        pr["menu"] = pr.menu 
        Item8 = tkinter.StringVar() 
        Item9 = tkinter.StringVar() 
        pr.menu.add_checkbutton ( label="Omnivore E", variable=Item8,onvalue="E") 
        pr.menu.add_checkbutton ( label="Carnivore F", variable=Item9,onvalue="F") 
        
        tkinter.Label(nwC,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nwC,from_=90,to=110)
        rr.grid(row=4,column=1)
        tkinter.Label(nwC,text="hunting successful rate:").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwC,from_=1000,to=2000)
        hsr.grid(row=5,column=1)
        tkinter.Button(nwC,text="Set/Update",command=nwC_get).grid(row=6,column=1)
        tkinter.Button(nwC,text="Cancel",command=nwC_quit).grid(row=6,column=0)
       
        nwC.mainloop()
#window for D
def New_window_D():
        
        def nwD_get():
            D=animals("D",[],[],0,0,0)
            D.species=sp.get()
            D.amount=am.get()
            D.prey.append(Item10.get())
            D.prey.append(Item11.get())
            D.predator.append(Item12.get())
            D.predator.append(Item13.get())
            D.r_r=rr.get()
            D.h_s_r=hsr.get()
            print(D.species,D.amount,D.r_r,D.prey,D.h_s_r,D.predator)
        def nwD_quit():
            nwD.destroy()
        nwD=tkinter.Toplevel()
        tkinter.Label(nwD,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nwD,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nwD,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nwD,bd=5,textvariable=tkinter.StringVar(value=""))
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
        am=tkinter.Entry(nwE,bd=5,textvariable=tkinter.StringVar(value=""))
        am.grid(row=1,column=1)
        
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
         
        pr.menu.add_checkbutton ( label="carnivore F", variable=Item18,onvalue="F")
        tkinter.Label(nwE,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nwE,from_=90,to=110)
        rr.grid(row=4,column=1)
        tkinter.Label(nwE,text="hunting successful rate:").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nwE,from_=100,to=1000)
        hsr.grid(row=5,column=1)
        def nwE_get():
            
  
            E=animals("E",[],[],0,0,0)
            E.species=sp.get()
            E.amount=am.get()
            E.prey.append(Item14.get())
            E.prey.append(Item15.get())
            E.prey.append(Item16.get())
            E.prey.append(Item17.get())
            E.predator.append(Item18.get())
            E.r_r=rr.get()
            E.h_s_r=hsr.get()
            print(E.species,E.amount,E.r_r,E.prey,E.h_s_r,E.predator)
        tkinter.Button(nwE,text="Set/Update",command=nwE_get).grid(row=6,column=1)
        tkinter.Button(nwE,text="Cancel",command=nwE_quit).grid(row=6,column=0)
       
        nwE.mainloop() 
#window for F            
def New_window_F():
        
            
        def nwF_quit():
            nw.destroy()
        nw=tkinter.Toplevel()
        tkinter.Label(nw,text="species:").grid(row=0,column=0)
        content=tkinter.StringVar(value="name")
        
        sp=tkinter.Entry(nw,bd=5,textvariable=content)
        sp.grid(row=0,column=1)
        
        tkinter.Label(nw,text="amount:").grid(row=1,column=0)
        am=tkinter.Entry(nw,bd=5,textvariable=tkinter.StringVar(value=""))
        am.grid(row=1,column=1)
        
        tkinter.Label(nw,text="prey:").grid(row=2,column=0)
        py=tkinter.Menubutton(nw,text="choose:")
        py.grid(row=2,column=1)
        py.menu = tkinter.Menu ( py, tearoff = 0 ) 
        py["menu"] = py.menu 
        Item19 = tkinter.StringVar() 
        Item20= tkinter.StringVar() 
        Item21= tkinter.StringVar()
        py.menu.add_checkbutton ( label="Herbivore C", variable=Item19) 
        py.menu.add_checkbutton ( label="Herbivore D", variable=Item20) 
        py.menu.add_checkbutton ( label="Omnivore E", variable=Item21,onvalue="88")
        #predator choice not available in F
        tkinter.Label(nw,text="predator:",state="disabled").grid(row=3,column=0)
        pr=tkinter.Menubutton(nw,text="choose:",state="disabled")
        pr.grid(row=3,column=1)
        
        tkinter.Label(nw,text="reproduce rate:").grid(row=4,column=0)
        rr=tkinter.Spinbox(nw,from_=90,to=110)
        rr.grid(row=4,column=1)
        tkinter.Label(nw,text="hunting successful rate:").grid(row=5,column=0)
        hsr=tkinter.Spinbox(nw,from_=0,to=50)
        hsr.grid(row=5,column=1)
        def nwF_get():
            F=animals("F",[],[],0,0,0)
            F.species=sp.get()
            F.amount=am.get()
            F.prey.append(Item19.get())
            F.prey.append(Item20.get())
            F.prey.append(Item21.get())
            F.r_r=rr.get()
            F.h_s_r=hsr.get()
            print(F.species,F.amount,F.r_r,F.prey,F.h_s_r,F.predator)
        tkinter.Button(nw,text="Set/Update",command=nwF_get).grid(row=6,column=1)
        tkinter.Button(nw,text="Cancel",command=nwF_quit).grid(row=6,column=0)
       
        nw.mainloop()
        
    
        


# set the parent window
pw=tkinter.Tk()

pw.resizable(False,False)

#labels
title_label = tkinter.Label(pw,text="Ecosystem Simulation", bg="white").grid(row=0,column=0,columnspan=3)
tkinter.Label(pw,text="Carnivore F", bg="white").grid(row=4,column=0,columnspan=2)
tkinter.Label(pw,text="Omnivore E",bg="white").grid(row=6,column=0,columnspan=2)
tkinter.Label(pw,text="Herbivore C", bg="white").grid(row=8,column=0)
tkinter.Label(pw,text="Herbivore D", bg="white").grid(row=8,column=1)
tkinter.Label(pw,text="Plant A", bg="white").grid(row=10,column=0)
tkinter.Label(pw,text="Plant B",bg="white").grid(row=10,column=1)
#buttons
bt1=tkinter.Button(pw,text="Carnivore F", bg="white",width=10,height=5,command=New_window_F).grid(row=3,column=0,columnspan=2)
bt2=tkinter.Button(pw,text="Omnivore E",bg="white",width=10,height=5,command=New_window_E).grid(row=5,column=0,columnspan=2)
bt3=tkinter.Button(pw,text="Herbivore C", bg="white",width=10,height=5,command=New_window_C)
bt3.grid(row=7,column=0)
bt4=tkinter.Button(pw,text="Herbivore D", bg="white",width=10,height=5,command=New_window_D).grid(row=7,column=1)
bt5=tkinter.Button(pw,text="Plant A", bg="white",width=10,height=5,command=New_window_A).grid(row=9,column=0)
bt6=tkinter.Button(pw,text="Plant B",bg="white",width=10,height=5,command=New_window_B).grid(row=9,column=1)

pw.mainloop()

  
time=input("times:")#set running years
#set amount of prey to be eaten
l=[A.amount,B.amount,C.amount*C.h_s_r,D.amount*D.h_s_r,E.amount*E.h_s_r,F.amount*F.h_s_r]
d=["A","B","C","D","E","F"]
totalA=0
totalB=0
totalC=0
totalD=0
totalE=0
for i in range (0,int(time)):
    print("time",i,":")
    for ii in range(0,len(A.grasseater)):
        x=d.index(A.grasseater[ii])
        print(x,l[x])
        totalA+=l[x]
        print(totalA)
    A.amount=A.amount*A.grow/100-totalA
    print("A:",A.amount)
    for ii in range(0,len(B.grasseater)):
        x=d.index(B.grasseater[ii])
        totalB+=l[x]
    B.amount=B.amount*B.grow/100-totalB
    print("B:",B.amount)
    for ii in range(0,len(C.predator)):
        x=d.index(C.predator[ii])
        totalC+=l[x]
    C.amount=C.amount*C.r_r/100-totalC
    print("C:",C.amount)
    for ii in range(0,len(D.predator)):
        x=d.index(D.predator[ii])
        totalD+=l[x]
    D.amount=D.amount*D.r_r/100-totalD
    print("D:",D.amount)
    for ii in range(0,len(E.predator)):
        x=d.index(E.predator[ii])
        totalE+=l[x]
    E.amount=E.amount*E.r_r/100-totalE
    print("E:",E.amount)
    
    F.amount=F.amount*F.r_r/100
    print("F:",F.amount)