#This is a GUI program using classes for organization


#Read - import required modules
import tkinter
import sys
from math import *
from tkinter import font
from tkinter import messagebox


#MenuBar class - called by the main class
class MenuBar(tkinter.Menu):
    #roots - opens a new top level window named filewin
    def roots(self):
        filewin = tkinter.Toplevel(self, bg="white")
        #Use grid to organize all of the widgets - labels, entries, buttons
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        self.title_label = tkinter.Label(filewin,text="Enter quadratic coefficients, a, b and c",font=helv18b, bg="white").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="a coefficient:",font=helv16, bg="white").grid(row=1,column=0)
        self.a_label=tkinter.Label(filewin,text="b coefficient:",font=helv16, bg="white").grid(row=2,column=0)
        self.a_label=tkinter.Label(filewin,text="c coefficient:",font=helv16, bg="white").grid(row=3,column=0)
        self.button_label=tkinter.Label(filewin,text="Calculate:",font=helv16, bg="white").grid(row=4,column=0)
        self.r1_label=tkinter.Label(filewin,text="First Root:",font=helv16, bg="white").grid(row=5,column=0)
        self.r2_label=tkinter.Label(filewin,text="Second Root:",font=helv16, bg="white").grid(row=6,column=0)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.a_entry.grid(row=1,column=1)
        self.b_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.b_entry.grid(row=2,column=1) 
        self.c_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.c_entry.grid(row=3,column=1)
        self.calculate = tkinter.Button(filewin, text="Enter", command=self.calculateRoots, font=helv16, bg="green")
        self.calculate.grid(row=4,column=1)
        #(float(a_entry.Get()), float(b_entry.Get()),float(c_entry.Get())))
        self.rootsLabel1 = tkinter.Label(filewin, textvariable=self.r1, font=helv16, bg="white")
        self.rootsLabel1.grid(row=5,column=1)
        self.rootsLabel2 = tkinter.Label(filewin, textvariable=self.r2, font=helv16, bg="white")
        self.rootsLabel2.grid(row=6,column=1)
     
    #Make the mathematical calculations - solves the roots problem 
    def calculateRoots(self):
        #Read values from Entry widgets using get()
        self.a = float(self.a_entry.get()) #convert from string to float 
        self.b = float(self.b_entry.get())
        self.c = float(self.c_entry.get())
        delta = self.b*self.b-4*self.a*self.c #b^2-4ac
        if delta > 0:
            #To change the value of the labels, use set()
            #Change the variable inside the label, not the label
            self.r1.set(str((-self.b+sqrt(delta))/(2*self.a)))
            self.r2.set(str((-self.b-sqrt(delta))/(2*self.a)))
        elif delta == 0:
            self.r1.set(str(-self.b/(4*self.a*self.c)))
            self.r2.set("No second root")
        else:
            self.r1.set("No Roots")
            self.r2.set("")
            
        print (self.r1.get())

    def tangentroots(self):
        filewin = tkinter.Toplevel(self, bg="white")
        #Use grid to organize all of the widgets - labels, entries, buttons
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        self.title_label = tkinter.Label(filewin,text="Enter quadratic coefficients, a, k ,c and d",font=helv18b, bg="white").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="a:",font=helv16, bg="white").grid(row=1,column=0)
        self.a_label=tkinter.Label(filewin,text="k:",font=helv16, bg="white").grid(row=2,column=0)
        self.a_label=tkinter.Label(filewin,text="c:",font=helv16, bg="white").grid(row=3,column=0)
        self.a_label=tkinter.Label(filewin,text="d:",font=helv16, bg="white").grid(row=4,column=0)
        self.button_label=tkinter.Label(filewin,text="Calculate:",font=helv16, bg="white").grid(row=5,column=0)
        self.r1_label=tkinter.Label(filewin,text="Answer:",font=helv16, bg="white").grid(row=6,column=0)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.a_entry.grid(row=1,column=1)
        self.k_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.k_entry.grid(row=2,column=1) 
        self.c_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.c_entry.grid(row=3,column=1)
        self.d_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.d_entry.grid(row=4,column=1)
        self.calculate = tkinter.Button(filewin, text="Enter", command=self.calculateRoots, font=helv16, bg="green")
        self.calculate.grid(row=5,column=1)
        #(float(a_entry.Get()), float(k_entry.Get()),float(c_entry.Get()))),float(d_entry.Get())))
        self.rootsLabel = tkinter.Label(filewin, textvariable=self.r, font=helv16, bg="white")
        self.rootsLabel.grid(row=6,column=1)
   
     
    #Make the mathematical calculations - solves the tangentroots problem 
    def calculateRoots(self):
        #Read values from Entry widgets using get()
        self.a = float(self.a_entry.get())  #convert from string to float 
        self.k = float(self.k_entry.get())
        self.c = float(self.c_entry.get())
        self.d = float(self.d_entry.get())
        self.y = self.a*tan(self.k * (self.c)) + self.d
        self.r.set(str(self.y))



    def Y(self):
        filewin = tkinter.Toplevel(self, bg="dark blue") 
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        self.title_label = tkinter.Label(filewin,text="Enter the values in below, a, k, d and c",font=helv18b, bg="white").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="a:",font=helv16, bg="white").grid(row=1,column=0)
        self.k_label=tkinter.Label(filewin,text="k:",font=helv16, bg="white").grid(row=2,column=0)
        self.d_label=tkinter.Label(filewin,text="d:",font=helv16, bg="white").grid(row=3,column=0)
        self.c_label=tkinter.Label(filewin,text="c:",font=helv16, bg="white").grid(row=4,column=0)
        self.y_label=tkinter.Label(filewin,text="y-value is:",font=helv16, bg="yellow").grid(row=6,column=0)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.a_entry.grid(row=1,column=1)
        self.k_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.k_entry.grid(row=2,column=1)        
        self.d_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.d_entry.grid(row=3,column=1)      
        self.c_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.c_entry.grid(row=4,column=1)       
        self.calculate = tkinter.Button(filewin, text="Enter", command=self.calculateY, font=helv16, bg="green")
        self.calculate.grid(row=5,column=1)
        self.y_label=tkinter.Label(filewin,textvariable=self.y,font=helv16, bg="yellow")
        self.y_label.grid(row=6,column=1)
      
    def calculateY(self):
        self.a=float(self.a_entry.get())
        self.k=float(self.k_entry.get())
        self.d=float(self.d_entry.get())
        self.c=float(self.c_entry.get())
        self.y.set(str(self.a * sin(self.k * (3.2 + self.d)) + self.c))
        print (self.y)
    



    def CosineLaw(self):
        filewin = tkinter.Toplevel(self, bg="pink")
        #Use grid to organize all of the widgets - labels, entries, buttons
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        self.title_label = tkinter.Label(filewin,text="Enter the elements of the triangle:",font=helv18b, bg="pink").grid(row=0,column=1,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="a:",font=helv16, bg="pink").grid(row=1,column=1)
        self.a_label=tkinter.Label(filewin,text="b:",font=helv16, bg="pink").grid(row=2,column=1)
        self.a_label=tkinter.Label(filewin,text="c:",font=helv16, bg="pink").grid(row=3,column=1)
        self.b_label=tkinter.Label(filewin,text="∠A:",font=helv16, bg="pink").grid(row=4,column=1)
        self.b_label=tkinter.Label(filewin,text="∠B:",font=helv16, bg="pink").grid(row=5,column=1)
        self.b_label=tkinter.Label(filewin,text="∠C:",font=helv16, bg="pink").grid(row=6,column=1)


        self.a_entry = tkinter.Entry(filewin,bd=1,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.a_entry.grid(row=1,column=2)
        self.b_entry = tkinter.Entry(filewin,bd=1,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.b_entry.grid(row=2,column=2) 
        self.c_entry = tkinter.Entry(filewin,bd=1,textvariable=tkinter.StringVar(value="0"), font=helv16)
        self.c_entry.grid(row=3,column=2)
        self.button_label=tkinter.Label(filewin,text="Calculate:",font=helv16, bg="pink").grid(row=7,column=1)
        self.calculate = tkinter.Button(filewin, text="Enter", command=self.calculateCosineLaw, font=helv16, bg="light green")
        self.calculate.grid(row=7,column=2)
        #(float(a_entry.Get()), float(b_entry.Get()),float(c_entry.Get())))
        self.rootsLabel1 = tkinter.Label(filewin, textvariable=self.r1, font=helv16, bg="pink")
        self.rootsLabel1.grid(row=4,column=2)
        self.rootsLabel2 = tkinter.Label(filewin, textvariable=self.r2, font=helv16, bg="pink")
        self.rootsLabel2.grid(row=5,column=2)
        self.rootsLabel3 = tkinter.Label(filewin, textvariable=self.r3, font=helv16, bg="pink")
        self.rootsLabel3.grid(row=6,column=2)
        
     
    #Make the mathematical calculations - solves the roots problem 
    def calculateCosineLaw(self):
        #Read values from Entry widgets using get()
        self.a = float(self.a_entry.get()) #convert from string to float 
        self.b = float(self.b_entry.get())
        self.c = float(self.c_entry.get())

        self.A = degrees(acos((self.b*self.b+self.c*self.c-self.a*self.a)/(2*self.b*self.c)))
        self.r1.set(str(self.A))
        self.B = degrees(acos((self.a*self.a+self.c*self.c-self.b*self.b)/(2*self.a*self.c)))
        self.r2.set(str(self.B))
        self.C = degrees(acos((self.a*self.a+self.b*self.b-self.c*self.c)/(2*self.a*self.b)))
        self.r3.set(str(self.C))
        

        
        
         
    #Place holder function - allows the program to work partially
    def donothing(self):
        pass
    
    def __init__(self, parent):
        helv14b = font.Font(family="Helvetica",size=14,weight="bold")
        tkinter.Menu.__init__(self, parent)
        #Two special variables - r1 and r2 - members of the MenuBar class
        self.r1 = tkinter.StringVar()
        self.r2 = tkinter.StringVar()
        self.r3 = tkinter.StringVar()  
        quadMenu = tkinter.Menu(self, tearoff=False, font=helv14b)
        #self.add_cascade(label="File",underline=0, menu=fileMenu)
        #quadMenu.add_command(label="Exit", underline=1, command=self.quit)
        quadMenu.add_command(label="Roots", command=self.roots)
        quadMenu.add_command(label="Vertex", command=self.donothing)
        self.add_cascade(label="Quadratic Equations", menu=quadMenu)
        trigmenu = tkinter.Menu(self, tearoff=0,font=helv14b)
        trigmenu.add_command(label="Tangent Law", command=self.tangentroots)
        trigmenu.add_command(label="Calculate y-value", command=self.Y)
        trigmenu.add_command(label="Sine Law", command=self.donothing)
        trigmenu.add_command(label="Cosine Law", command=self.CosineLaw)
        self.add_cascade(label="Trigonometry", menu=trigmenu)
        ssmenu = tkinter.Menu(self, tearoff=0, font=helv14b)
        ssmenu.add_command(label="Arithmetic Sequences", command=self.donothing)
        ssmenu.add_command(label="Geometric Sequences", command=self.donothing)                
        ssmenu.add_command(label="Arithmetic Series", command=self.donothing)
        ssmenu.add_command(label="Geometric Series", command=self.donothing)
        self.add_cascade(label="Discrete", menu=ssmenu)
        physicsmenu = tkinter.Menu(self, tearoff=0, font=helv14b)
        physicsmenu.add_command(label="Projectiles", command=self.donothing)
        physicsmenu.add_command(label="Momentum", command=self.donothing)
        self.add_cascade(label="Physics", menu=physicsmenu)
        datamenu = tkinter.Menu(self, tearoff=0, font=helv14b)
        datamenu.add_command(label="Factorials", command=self.donothing)
        datamenu.add_command(label="Combinations", command=self.donothing)
        datamenu.add_command(label="Permutations", command=self.donothing)        
        datamenu.add_command(label="Geometric Distribution", command=self.donothing)        
        datamenu.add_command(label="Hypergeometric Distribution", command=self.donothing)        
        
        self.add_cascade(label="Data", menu=datamenu)
        calculusmenu = tkinter.Menu(self, tearoff=0, font=helv14b)
        calculusmenu.add_command(label="Derivatives", command=self.donothing)
        calculusmenu.add_command(label="Integrals", command=self.donothing)
        calculusmenu.add_command(label="Newton's Method", command=self.donothing)        
        self.add_cascade(label="Calculus", menu=calculusmenu)
        #This part adds a background picture (must be in the same directory and in .gif format)
        self.canvas = tkinter.Canvas(parent,width=400,height=400,bg="white")
        self.filename=tkinter.PhotoImage(master=self.canvas, file="D:\莹莹\MathBackground.gif.gif")
        self.image1=self.canvas.create_image(10,10,image=self.filename)
        self.canvas.pack()

    def quit(self):
        sys.exit(0)
        
#Main class - calls menubar class
class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.geometry("420x400")
        self.title("Math Problem Solver")
        self.config(menu=menubar)

#Start the program:
if __name__ == "__main__":
    app=App()
    app.mainloop()
