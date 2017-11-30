

#from Tkinter import *
#import pyserial
#import cv2
#from cv2 import *
#from PIL import Image, ImageTk
import tkinter

class Arduino:
    def writechar(self, char):
        print ("Sending ", char, " to the Arduino")
        #self.connection1.write(char)
        #s = self.connection1.read(21)        # read up to ten bytes (timeout)
        #line = self.connection1.readline()   # read a '\n' terminated line
        #print s, line

    def connection(self):
        pass
        #return  pyserial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0.1)

    
class App:
    def __init__(self,parent):
        #The frame instance is stored in a local variable 'f'.
        #After creating the widget, we immediately call the 
        #pack method to make the frame visible.

        f = tkinter.Frame(parent, background = "black", width = 600)
        f.pack()
        
        #we then create an entry widget,pack it and then 
        #create two more button widgets as children to the frame.
    
        #self.entry = Entry(f,text="enter your choice")
        #self.entry.pack(side= TOP,padx=10,pady=12)
        
        #this time, we pass a number of options to the
        # constructor, as keyword arguments. The first button
        # is labelled "exit"and the second is labelled "Hello". 
        #Both buttons also take a command option. This option 
        #specifies a function, or (as in this
        #case) a bound method, which will be called when the button is clicked.
        
        self.opendoor = tkinter.Button(f, text="openthedoor", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.opendoor).grid(row=0, column=0)
        self.trackmode = tkinter.Button(f, text="TrackMode", font = "Arial 24 bold",background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.trackmode).grid(row=1, column=0)
        self.sit = tkinter.Button(f, text="Sitdown", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow", height=2, width=10,command=self.sit).grid(row=0, column=1)
        self.carforward = tkinter.Button(f, text="Forward", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.carforward).grid(row=1, column=1)
        self.fastenseatbelt = tkinter.Button(f, text="Seatbelt On", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow", height=2, width=10,command=self.fastenseatbelt).grid(row=0, column=2)
        self.ecomode = tkinter.Button(f, text="Ecomode", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.ecomode).grid(row=1, column=2)
        self.carengineon = tkinter.Button(f, text="engine on", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow", height=2, width=10,command=self.carengineon).grid(row=0, column=3)
        self.carturnleft = tkinter.Button(f, text="Turn Left", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.carturnleft).grid(row=2, column=0)
        self.carbrake= tkinter.Button(f, text="Brake", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.carbrake).grid(row=2, column=1)
        self.carturnright = tkinter.Button(f, text="Turn Right", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.carturnright).grid(row=2, column=2)
        self.carbackward= tkinter.Button(f, text="Backward", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.carbackward).grid(row=3, column=1)
        self.manualdrive = tkinter.Button(f, text="ManualDrive", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.manualdrive).grid(row=3, column=2)
        self.carengineoff = tkinter.Button(f,text="engine off", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.carengineoff).grid(row=1, column=3)
        self.unfastenseatbelt = tkinter.Button(f,text="unfasten SB", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.unfastenseatbelt).grid(row=2, column=3)
        self.leavethecar = tkinter.Button(f,text="leave the car", font = "Arial 24 bold", background = "white",foreground = "black", activebackground="yellow",height=2, width=10,command=self.leavethecar).grid(row=3, column=3)


        self.autodrive = tkinter.Button(f, text="AutoDrive", font = "Arial 24 bold", background = "red",foreground = "white", activebackground="yellow", height=2, width=10,command=self.autodrive).grid(row=3,column=0)
        self.openlight = tkinter.Button(f,background = "black",activebackground="white",foreground = "white",text="headlight on", font = "Arial 24 bold", height=2, width=10,command=self.openlight).grid(row=4,column=0)
        self.closelight = tkinter.Button(f, background = "red", activebackground="white",foreground = "white", text="headlight off", font = "Arial 24 bold", height=2, width=10,command=self.closelight).grid(row=4,column=1)
        self.exit = tkinter.Button(f, text="Exit", font = "Arial 24 bold", activebackground="red",foreground = "white", background = "green", height=2, width=10, command=f.destroy).grid(row=4,column=3)


        #self.im = Image.open("heli.jpg")
        #self.im1 = PhotoImage(self.im)
        #self.helipic = Label(f, image=self.im1, width = 200, height = 200).grid(row=1,column=3,rowspan=2)
        #self.disp = Label(f, width = 200, height = 100, background = "purple")
#        C:\Users\gwilm\Documents\NCCI\MCV4U\3D - Motion Tracker\OO_Dev\
        #sself.disp.pack(side = RIGHT)

    def print_this(self):
        print ("this is to be printed")

        #Finally, we provide some script level code that creates
        # a Tk root widget,and one instance of the App class using 
        #the root widget as its parent:

        #The last call is to the mainloop method on the root widget. It enters the
        #Tk event loop, in which the application will stay until the quit method is
        #called (just click the exit button), or the window is closed.
    def opendoor(self):
        print ("The door has opened for you.")
        Arduino_Conn.writechar("A255")
        

    def sit(self):
        print ("You're already in the car.")
        Arduino_Conn.writechar("A125")
        

    def fastenseatbelt(self):
        print ("You have fastened your seat belt.")
        Arduino_Conn.writechar("A100")
        
    def carengineon(self):
        print ("The car has strated")
        Arduino_Conn.writechar("A000")

    def trackmode(self):
        print ("Track Mode has opened")
        Arduino_Conn.writechar("D250")

    def carforward(self):
        print("Car is moving forward")
        Arduino_Conn.writechar("D000")

    def ecomode(self):
        print ("ECO Mode has opened")
        Arduino_Conn.writechar("D080")

    def carbackward(self):
        print("Car is moving backward")
        Arduino_Conn.writechar("C128")
        
    def manualdrive(self):
        print ("Manual Drive has opened")
        Arduino_Conn.writechar("B000")

    def carbrake(self):
        print ("Car is braking")
        Arduino_Conn.writechar("B100")

    def carturnleft(self):
        print ("Car is turning left")
        Arduino_Conn.writechar("B911")

    def carturnright(self):
        print ("Car is turning right")
        #print "Helicopter moving right"
        Arduino_Conn.writechar("B255")
        
    def carengineoff(self):
        print("Car is shutting down")
        Arduino_Conn.writechar("B666")
        
    def unfastenseatbelt(self):   
        print ("unfastenseatbelt")
        Arduino_Conn.writechar("B999")
        
    def leavethecar(self):
        print ("you are leaving the car")
        Arduino_Conn.writechar("B111")
        

    def throttle(self, level):
        level = int(level)
        if level < 0:
            level = 0
        if level >255:
            level = 255
            
        if level < 10:
            Arduino_Conn.writechar("A00"+str(level))
        elif level < 100:
            Arduino_Conn.writechar("A0"+str(level))
        else:
            Arduino_Conn.writechar("A"+str(level))

    def autodrive(self):
            count = 0
            delaytime = 1200
            while count < 18:
                self.throttle(200)
                self.helicopterleft()
                delay = 0
                while delay < delaytime:
                    delay +=1
                count +=1
            count = 0
            while count < 18:
                self.throttle(100)
                #self.helicopterbackwards()
                #self.helicopterright()
                delay = 0
                while delay < delaytime:
                    delay +=1
                count +=1
            count = 0
            #self.helicoptervy0()
            while count < 38:
                self.throttle(50)
                #self.helicopterleft() 
                delay = 0
                while delay < delaytime:
                    delay +=1
                count +=1
            self.throttle(0)
            self.helicoptervx0()
            
                
                 
    def openlight(self):
        print ("The connection to the arduino is being established")
        Arduino_Conn.connection1 = Arduino_Conn.connection()
        print ("The connection seems to have been established")
    
    def closelight(self):
        Arduino_Conn.connection1.flushInput()
        Arduino_Conn.connection1.flushOutput()
        Arduino_Conn.connection1.close()
        print ("Disconnected")
        

Arduino_Conn = Arduino()
 
root = tkinter.Tk()
root.title('Car Simulator')
app = App(root)

root.mainloop()
