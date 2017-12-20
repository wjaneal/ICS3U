#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:31:36 2017
@author: chenquancheng
"""
import serial
from tkinter import *
import sys
from tkinter import font
import math

class MenuBar(Menu): #creates a MenuBar class
   
    def writechar(self, byte1):
        '''
        sends messages to Arduino
        Parameters:
            self - MenuBar
            byte1 - byte - message sent to Arduino
        Return - None
        '''
        print ("Sending ", byte1, " to the Arduino") #prints a message in python to show that the message is being sent to Arduino 
        self.connection1.write(byte1)         # sends the message to Arduino
        s = self.connection1.read(21)        # read up to ten bytes (timeout)
        line = self.connection1.readline()   # read a '\n' terminated line
        print (s, line)                      # prints in python
    

    def connection(self):
        '''
        Connects to Arduino
        Parameters:
            self - MenuBar
        '''
        return serial.Serial('/dev/tty.usbmodem1461', baudrate=9600, timeout=0.1)
        
        
        #return  pyserial.Serial('COM3', baudrate=9600, timeout=0.1)
    def new(self):
        helv18b = font.Font(family="Helvetica",size=18,weight="bold") #defines fonts
        helv16 = font.Font(family="Helvetica",size=16,weight="bold") #defines fonts
        filewin = Toplevel(self) #opens a new window
        self.C = Canvas(filewin) #creates a rectangular area intended for drawing pictures
        self.oval = self.C.create_oval(10,10,60,60, fill="red") #creates an oval which shows whether the state is on or off
        self.C.grid(row=0,column=0,columnspan=5) #places the oval
        self.label=self.C.create_text((35,35),text="Status",font=helv16) #creates a label which displays the word "status"
        self.start_button = Button(filewin,text="Start",command=self.start).grid(row=1,column=0) #creates a button which starts scanning
        self.stop_button = Button(filewin,text="Stop",command=self.stop).grid(row=2,column=0) #creates a button which stops scanning
        self.scand=Label(filewin,text="Scan Dimensions:").grid(row=3,column=0) #creates a label which displays "Scan Dimensions:"
        self.scanx=Label(filewin,text="x").grid(row=4,column=0) #creates a label which displays "x"
        self.scany=Label(filewin,text="y").grid(row=5,column=0) #creates a label which displays "y"
        self.x_entry = Entry(filewin,bd=5,width=1,textvariable=StringVar(value="0")) #reads the x value
        self.x_entry.grid(row=4,column=1) #places the entry for the x value
        self.y_entry = Entry(filewin,bd=5,width=1,textvariable=StringVar(value="0")) #reads the y value
        self.y_entry.grid(row=5,column=1) #places the entry for the y value
        self.xunits=Label(filewin,text="nm").grid(row=4,column=2) #displays the units for x-nm
        self.yunits=Label(filewin,text="nm").grid(row=5,column=2) #displays the units for y-nm
        self.coordinates=Label(filewin,text="Current x-y Coordinates:").grid(row=6,column=0) #creates a label which displays "Current x-y Coordinates:"
        self.currentCx=Label(filewin,text="x").grid(row=7,column=0) #creates a label which displays "x"
        self.currentCy=Label(filewin,text="y").grid(row=8,column=0) #creates a label which displays "y"
        self.x_coordinate=Label(filewin,textvariable=self.currentx).grid(row=7,column=1) #creates a label which displays the current x-coordinate
        self.y_coordinate=Label(filewin,textvariable=self.currenty).grid(row=8,column=1) #creates a label which displays the current y-coordinate
        self.voltages=Label(filewin,text="Voltages:").grid(row=9,column=0) #creates a label which displays "Voltages:"
        self.x_voltage=Label(filewin,text="x").grid(row=10,column=0) #creates a label which displays "x"
        self.y_voltage=Label(filewin,text="y").grid(row=11,column=0) #creates a label which displays "x"
        self.creading=Label(filewin,text="Current Reading").grid(row=12,column=0) #creates a label which displays "Current Reading"
        self.scan=Label(filewin,text="Scan Display",font=helv18b).grid(row=0,column=3) #creates a label which displays "Scan Display"
        #generates some random curves
        self.line1 = self.C.create_line(220,100,320,160,fill="blue")
        self.line2 = self.C.create_line(200,180,300,170,fill="green")
        self.coord = 220,90,300,150
        self.arc = self.C.create_arc(self.coord, start=0, extent=150, fill="yellow")
        

   
    def start(self):
        '''
        makes the status on(makes the button green)
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.C.itemconfig(self.oval, fill="green")
    
    def stop(self):
        '''
        makes the status off(makes the button red)
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.C.itemconfig(self.oval,fill="red")
        
        
    def donothing(self):
        '''
        does nothing
        Parameters:
            self - MenuBar
        Return - None
        '''
        pass
    
    
    def __init__(self, parent):
        Menu.__init__(self, parent)
        self.dx = StringVar() #creates a Tkinter variable dx
        self.dy = StringVar() #creates a Tkinter variable dy
        self.currentx = StringVar() #creates a Tkinter variable currentx
        self.currenty = StringVar() #creates a Tkinter variable currenty
        filemenu = Menu(self, tearoff=0) #creates a filemenu
        filemenu.add_command(label="New", command=self.new) #adds a "New" command to the filemenu
        filemenu.add_command(label="Open", command=self.donothing) #adds a "Open" command to the filemenu
        filemenu.add_command(label="Save", command=self.donothing) #adds a "Save" command to the filemenu
        filemenu.add_command(label="Save as...", command=self.donothing) #adds a "Save as..." command to the filemenu
        self.add_cascade(label="File", menu=filemenu) #names the filemenu "File"
        settingsmenu = Menu(self, tearoff=0)  #creates a settingsmenu
        settingsmenu.add_command(label="Calibrate", command=self.donothing) #adds a "Calibrate" command to the settingsmenu
        filemenu.add_command(label="Exit", command=self.quit) #adds a "Exit" command to the settingsmenu
        self.add_cascade(label="Settings", menu=settingsmenu) #names the settingsmenu "Settings"
        helpmenu = Menu(self, tearoff=0) #creates a helpmenu
        helpmenu.add_command(label="Help Index", command=self.donothing) #adds a "Help Index" command to the helpmenu 
        helpmenu.add_command(label="About...", command=self.donothing) #adds a "About..." command to the helpmenu 
        self.add_cascade(label="Help", menu=helpmenu) #names the helpmenu "Help"
        arduinomenu = Menu(self, tearoff=0) #creates an arduinomenu
        arduinomenu.add_command(label="Connect",command=self.connect) #adds a "Connect" command to the arduinomenu
        arduinomenu.add_command(label="Disconnect",command=self.disconnect) #adds a "Disconnect" command to the arduinomenu
        self.add_cascade(label="Arduino",menu=arduinomenu) #names the arduinomenu "Arduino"
        
        self.pin2=Button(parent,text="pin2",command=self.pin2).grid(row=0,column=1) #creates a button for pin2
        self.pin3=Button(parent,text="pin3",command=self.pin3).grid(row=0,column=2) #creates a button for pin3
        self.pin4=Button(parent,text="pin4",command=self.pin4).grid(row=0,column=3) #creates a button for pin4
        self.pin5=Button(parent,text="pin5",command=self.pin5).grid(row=0,column=4) #creates a button for pin5
        self.pin6=Button(parent,text="pin6",command=self.pin6).grid(row=0,column=5) #creates a button for pin6
    
    def pin2(self):
        '''
        sends a message to Arduino for pin2
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"A250") #sends A250 to Arduino
    
    def pin3(self):
        '''
        sends a message to Arduino for pin3
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"B125") #sends B125 to Arduino
        
    def pin4(self):
        '''
        sends a message to Arduino for pin4
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"C000") #sends C000 to Arduino
    
    def pin5(self):
        '''
        sends a message to Arduino for pin5
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"D125") #sends D125 to Arduino
    
    def pin6(self):
        '''
        sends a message to Arduino for pin6
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"E250") #sends E250 to Arduino
    
    def pin7(self):
        '''
        sends a message to Arduino for pin7
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"F500") #sends F500 to Arduino
    
    def pin8(self):
        '''
        sends a message to Arduino for pin8
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"G125") #sends G125 to Arduino
    
    def pin9(self):
        '''
        sends a message to Arduino for pin9
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"H125") #sends H125 to Arduino
    
    def pin10(self):
        '''
        sends a message to Arduino for pin10
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"I250") #sends I250 to Arduino
    
    def pin11(self):
        '''
        sends a message to Arduino for pin11
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"J125") #sends J125 to Arduino
        
    def pin12(self):
        '''
        sends a message to Arduino for pin12
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"K500") #sends K500 to Arduino
    
    def pin13(self):
        '''
        sends a message to Arduino for pin13
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.writechar(b"L500") #sends L500 to Arduino
    
    
    def connect(self):
        '''
        connects to Arduino
        Parameters:
            self - MenuBar
        Return - None
        '''
        print ("The connection to the arduino is being established") #prints a message in python to show that the connection to Arduino is being established
        self.connection1 = self.connection() #connects to Arduino
        print ("The connection seems to have been established")
        #prints a message in python to show that the connection to Arduino has been established
        
    def disconnect(self):
        '''
        disconnects from Arduino
        Parameters:
            self - MenuBar
        Return - None
        '''
        self.connection1.flushInput()
        self.connection1.flushOutput()
        self.connection1.close()
        print ("Disconnected")
        #prints a message in python to show that it has been disconnected from Arduino
        
    def quit(self):
        '''
        quits the program
        Parameters:
            self - MenuBar
        Return - None
        '''
        app.destroy() #quits the program


          
#Main class - calls menubar class
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)


#Start the program:
if __name__ == "__main__":
    app=App()
    app.title('Scanning Tunneling Microscope')
    app.mainloop()
