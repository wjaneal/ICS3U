#Here is a program about putting a classical game, scissors, rock and paper into
#the tkinter, so that the players can have a better experience.In the game, you
#can print which one do you want to use. At the same time, the label will show
#the computer's choice and show the final result.
import tkinter
import sys
import random
from math import *
from tkinter import font
#define a class about the menu.
class MenuBar(tkinter.Menu):
    #define the basis window of the SRP
    def SRP(self):
        filewin = tkinter.Toplevel(self)
        self.title_label = tkinter.Label(filewin,text="Scissors, rock and paper!").grid(row=0,column=0,columnspan=2)
        self.a_label=tkinter.Label(filewin,text="Your choice:").grid(row=1,column=0)
        self.button_label=tkinter.Label(filewin,text="Concern:").grid(row=3,column=0)
        self.x_label=tkinter.Label(filewin,text="Computer's choice:").grid(row=5,column=0)
        self.y_label=tkinter.Label(filewin,text="Final result:").grid(row=6,column=0)
        self.concern = tkinter.Button(filewin, text="Enter", command=self.concernResult)
        self.concern.grid(row=7,column=1)
        self.a_entry = tkinter.Entry(filewin,bd=5,textvariable=tkinter.StringVar(value=""))
        self.a_entry.grid(row=3,column=1)
        self.xLabel = tkinter.Label(filewin, textvariable=self.x)
        self.xLabel.grid(row=5,column=1)
        self.yLabel = tkinter.Label(filewin, textvariable=self.y)
        self.yLabel.grid(row=6,column=1)
    #define the judge of the game
    def concernResult(self):
        self.a = self.a_entry.get()
        cs = int(random.random()*3) #computer's number
        #convert computer's number into a specific choice
        if cs == 0:
            self.x.set("Scissors")
        if cs == 1:
            self.x.set("Rock")
        if cs == 2:
            self.x.set("Paper")
        #judge whether the player win the game
        if self.a == "S" or self.a == "s" or self.a =="scissors":
            self.a = 0
        if self.a == "R" or self.a == "r" or self.a =="rock":
            self.a = 1
        if self.a == "P" or self.a == "p" or self.a =="paper":
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
    #define the basis window of Guess Number
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

    #define the judege of the game
    def concernResult2(self):
        newnum = ((random.random()*100)+1)
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
    
    #define which menu we don't need 
    def donothing(self):
        pass

    #define the basis window of the whole program
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
        gamesMenu.add_command(label="guess numbers", command=self.GuessNum)
        gamesMenu.add_command(label="Exit", command=self.quit)
        self.tip_label=tkinter.Label(text="SRP is finished! ").grid(row=6,column=0)
        self.tip1_label=tkinter.Label(text="You can input the first letter of SRP or print the whole name of them,").grid(row=7,column=0)
        self.tip2_label=tkinter.Label(text="like paper or rock.").grid(row=8,column=0)
        self.tip3_label=tkinter.Label(text="My new games are coming soon!").grid(row=9,column=0)
        self.tip4_label=tkinter.Label(text="Thanks for your playing!").grid(row=10,column=0)
    #define if you want to quit the program
    def quit(self):
        sys.exit()

#define the set of the game.
class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.geometry("420x400")
        self.title("Game Star")
        self.config(menu=menubar)

#show the window of the program
if __name__ == "__main__":
    app=App()
    app.mainloop()
