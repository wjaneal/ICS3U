import tkinter
import sys
import random
from math import *
from tkinter import font
class MenuBar(tkinter.Menu):
    def SRP(self):
        filewin = tkinter.Toplevel(self)
        self.title_label = tkinter.Label(filewin,text="Scissors, rock and paper!").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="Your choice:").grid(row=1,column=0)
        self.button_label=tkinter.Label(filewin,text="Concern:").grid(row=3,column=0)
        self.x_label=tkinter.Label(filewin,text="Computer's choice:").grid(row=5,column=0)
        self.y_label=tkinter.Label(filewin,text="Final result:").grid(row=6,column=0)
        self.concern = tkinter.Button(filewin, text="Enter", command=self.concernResult)
        self.concern.grid(row=7,column=1)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.a_entry.grid(row=3,column=1)
        self.xLabel = tkinter.Label(filewin, textvariable=self.x)
        self.xLabel.grid(row=5,column=1)
        self.yLabel = tkinter.Label(filewin, textvariable=self.y)
        self.yLabel.grid(row=6,column=1)
  
    def concernResult(self):
        self.a = self.a_entry.get()
        cs = int(random.random()*3)
        if cs == 0:
            self.x.set("Scissors")
        if cs == 1:
            self.x.set("Rock")
        if cs == 2:
            self.x.set("Paper")
        if self.a == "S" or self.a == "s":
            self.a = 0
        if self.a == "R" or self.a == "r":
            self.a = 1
        if self.a == "P" or self.a == "p":
            self.a = 2
        if self.a == 0 and cs == 1:
            self.y.set("You lose!")
        if self.a == 0 and cs == 2:
            self.y.set("You win!")
        if self.a == 1 and cs == 0:
            self.y.set("You win!")
        if self.a == 1 and cs == 2:
            self.y.set("You lose!")
        if self.a == 2 and cs == 0:
            self.y.set("You lose!")
        if self.a == 2 and cs == 1:
            self.y.set("You win!")
        if self.a == cs:
            self.y.set("Tie!")

    def GuessNum(self):
        filewin = tkinter.Toplevel(self)
        
        self.title_label = tkinter.Label(filewin,text="Guess Numbers!(1-100)").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="Your guess:").grid(row=1,column=0)
        self.button_label=tkinter.Label(filewin,text="Concern:").grid(row=3,column=0)
        self.x_label=tkinter.Label(filewin,text="Tips:").grid(row=5,column=0)
        self.y_label=tkinter.Label(filewin,text="The times you spend is:").grid(row=6,column=0)
        self.concern = tkinter.Button(filewin, text="Concern", command=self.concernResult2)
        self.concern.grid(row=8,column=1)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value="0"))
        self.a_entry.grid(row=3,column=1)
        self.xLabel = tkinter.Label(filewin, textvariable=self.x)
        self.xLabel.grid(row=5,column=1)
        self.yLabel = tkinter.Label(filewin, textvariable=self.y)
        self.yLabel.grid(row=6,column=1)

    def concernResult2(self):
        newnum = int(input("Print a number that you want others to guess:"))
        self.a = int(self.a_entry.get())
        c = 1
        while self.a != newnum:
            if newnum > self.a:
                c+=1
                self.x.set("Your guess is smaller than the number!")
            if newnum < self.a:
                c+=1
                self.x.set("Your guess is larger than the number!")
            self.y.set(c)
    
        
    def donothing(self):
        pass
    
    def __init__(self, parent):
        helv14b = font.Font(family="Helvetica",size=14,weight="bold")
        tkinter.Menu.__init__(self, parent)
        self.x = tkinter.StringVar()
        self.y = tkinter.StringVar()
        quadMenu = tkinter.Menu(self, tearoff=False, font=helv14b)
        self.add_cascade(label="File",underline=0, menu=quadMenu)
        quadMenu.add_command(label="Exit", underline=1, command=self.quit)
        gamesMenu = tkinter.Menu(self, tearoff=0, font=helv14b)
        self.add_cascade(label="Games", menu=gamesMenu)
        gamesMenu.add_command(label="SRP", command=self.SRP)
        gamesMenu.add_command(label="guess numbers", command=self.donothing)
        gamesMenu.add_command(label="Exit", command=self.quit)
        self.tip_label=tkinter.Label(text="SRP is finished! ").grid(row=6,column=0)
        self.tip1_label=tkinter.Label(text="Besides, through the experience.").grid(row=7,column=0)
        self.tip2_label=tkinter.Label(text="I found that Guess Number can't be played in the tkinter.").grid(row=8,column=0)
        self.tip3_label=tkinter.Label(text="My new games are coming soon!").grid(row=9,column=0)
        self.tip4_label=tkinter.Label(text="Thanks for your playing!").grid(row=10,column=0)
    
    def quit(self):
        sys.exit(0)


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.geometry("420x400")
        self.title("Game Star")
        self.config(menu=menubar)


if __name__ == "__main__":
    app=App()
    app.mainloop()
