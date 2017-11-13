#Read - import required modules
import tkinter
import sys
from tkinter import font
from tkinter import messagebox
#MenuBar class - called by the main class
class MenuBar(tkinter.Menu):
    def Emmatap(self):
        filewin = tkinter.Toplevel(self, bg="pink")
        #Use grid to organize all of the widgets - buttons
        helv18b = font.Font(family="Helvetica",size=18,weight="bold")
        helv16 = font.Font(family="Helvetica",size=16,weight="bold")
        self.title_label = tkinter.Label(filewin,text="Press to play",font=helv18b, bg="pink").grid(row=0,column=0,columnspan=2)
        self.button1 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button1.grid(row=4,column=1)
        self.button2 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button2.grid(row=5,column=1)
        self.button3 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button3.grid(row=4,column=2)
        self.button4 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button4.grid(row=5,column=2)
        self.button5 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button5.grid(row=4,column=3)
        self.button6 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button6.grid(row=5,column=3)
        self.button7 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button7.grid(row=4,column=4)
        self.button8 = tkinter.Button(filewin, text="", command=self.playEmmatap, font=helv16, bg="pink", bd=8, height=4, width=10)
        self.button8.grid(row=5,column=4)
        
    def __init__(self, parent):
        helv14b = font.Font(family="Helvetica",size=14,weight="bold")
        tkinter.Menu.__init__(self, parent)
        musicMenu = tkinter.Menu(self, tearoff=False, font=helv14b)
        #self.add_cascade(label="File",underline=0, menu=fileMenu)
        #quadMenu.add_command(label="Exit", underline=1, command=self.quit)
        musicMenu.add_command(label="Emmatap", command=self.Emmatap)
        self.add_cascade(label="Emmatap", menu=musicMenu)


    def playEmmatap(self):
        return


#Main class - calls menubar class
class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.title("Emmatap")
        self.config(menu=menubar)
            

#Start the program:
if __name__=="__main__":
    app=App()
    app.mainloop()
    
        

