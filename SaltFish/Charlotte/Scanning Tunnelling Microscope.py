#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:31:36 2017

@author: chenquancheng
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:19:48 2017

@author: chenquancheng
"""


from tkinter import *
import sys
from tkinter import font
import math

class Arduino(object):
    def writechar(self, char):
        print ("Sending ", char, " to the Arduino")
        """self.connection1.write(char)
        s = self.connection1.read(21)        # read up to ten bytes (timeout)
        line = self.connection1.readline()   # read a '\n' terminated line
        print (s, line)"""

    def connection(self):
        pass
        #return  pyserial.Serial('COM3', baudrate=9600, timeout=0.1)
        
Arduino_Conn = Arduino()

class MenuBar(Menu):
    def new(self):
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        filewin = Toplevel(self)
        #status = "off"
        self.C = Canvas(filewin)
        self.oval = self.C.create_oval(10,10,60,60, fill="red")
        self.C.grid(row=0,column=0,columnspan=5)
        self.label=self.C.create_text((35,35),text="Status",font=helv16)
        self.start_button = Button(filewin,text="Start",command=self.start).grid(row=1,column=0)
        self.stop_button = Button(filewin,text="Stop",command=self.stop).grid(row=2,column=0)
        self.scand=Label(filewin,text="Scan Dimensions:").grid(row=3,column=0)
        self.scanx=Label(filewin,text="x").grid(row=4,column=0)
        self.scany=Label(filewin,text="y").grid(row=5,column=0)
        self.x_entry = Entry(filewin,bd=5,width=1,textvariable=StringVar(value="0"))
        self.x_entry.grid(row=4,column=1)
        self.y_entry = Entry(filewin,bd=5,width=1,textvariable=StringVar(value="0"))
        self.y_entry.grid(row=5,column=1)
        self.xunits=Label(filewin,text="nm").grid(row=4,column=2)
        self.yunits=Label(filewin,text="nm").grid(row=5,column=2)
        self.coordinates=Label(filewin,text="Current x-y Coordinates:").grid(row=6,column=0)
        self.currentCx=Label(filewin,text="x").grid(row=7,column=0)
        self.currentCy=Label(filewin,text="y").grid(row=8,column=0)
        self.x_coordinate=Label(filewin,textvariable=self.currentx).grid(row=7,column=1)
        self.y_coordinate=Label(filewin,textvariable=self.currenty).grid(row=8,column=1)
        self.voltages=Label(filewin,text="Voltages:").grid(row=9,column=0)
        self.x_voltage=Label(filewin,text="x").grid(row=10,column=0)
        self.y_voltage=Label(filewin,text="y").grid(row=11,column=0)
        self.creading=Label(filewin,text="Current Reading").grid(row=12,column=0)
        self.scan=Label(filewin,text="Scan Display",font=helv18b).grid(row=0,column=3)
        #random curves
        self.line1 = self.C.create_line(220,100,320,160,fill="blue")
        self.line2 = self.C.create_line(200,180,300,170,fill="green")
        self.coord = 220,90,300,150
        self.arc = self.C.create_arc(self.coord, start=0, extent=150, fill="yellow")
        

   
    def start(self):
        #status = "on"
        self.C.itemconfig(self.oval, fill="green")
    
    def stop(self):
        #status = "off"
        self.C.itemconfig(self.oval,fill="red")
        
        
    def donothing(self):
        pass
    
    
    def __init__(self, parent):
        Menu.__init__(self, parent)
        self.dx = StringVar()
        self.dy = StringVar()
        self.currentx = StringVar()
        self.currenty = StringVar()
        filemenu = Menu(self, tearoff=0) 
        filemenu.add_command(label="New", command=self.new) 
        filemenu.add_command(label="Open", command=self.donothing) 
        filemenu.add_command(label="Save", command=self.donothing) 
        filemenu.add_command(label="Save as...", command=self.donothing)
        self.add_cascade(label="File", menu=filemenu) 
        settingsmenu = Menu(self, tearoff=0) 
        settingsmenu.add_command(label="Calibrate", command=self.donothing)
        filemenu.add_command(label="Exit", command=self.quit) 
        self.add_cascade(label="Settings", menu=settingsmenu)
        helpmenu = Menu(self, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing) 
        helpmenu.add_command(label="About...", command=self.donothing)
        self.add_cascade(label="Help", menu=helpmenu)
        arduinomenu = Menu(self, tearoff=0)
        arduinomenu.add_command(label="Connect",command=self.connect)
        arduinomenu.add_command(label="Disconnect",command=self.disconnect)
        self.add_cascade(label="Arduino",menu=arduinomenu)
        
    def connect(self):
        print ("The connection to the arduino is being established")
        Arduino_Conn.connection1 = Arduino_Conn.connection()
        Arduino_Conn.writechar("A255")
        print ("The connection seems to have been established")
    
    def disconnect(self):
        Arduino_Conn.connection1.flushInput()
        Arduino_Conn.connection1.flushOutput()
        Arduino_Conn.connection1.close()
        print ("Disconnected")
        
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
    app.title('Scanning Tunnelling Microscope')
    app.mainloop()