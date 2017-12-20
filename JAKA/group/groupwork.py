from tkinter import *
import tkinter
import random

'''separate player's choice and computer's choice in two lists
player's choice：list2
computer's choice: list1'''
list2=[4,4,4,4]#initial the elements to ensure none is correct at the beginning
list1=[]
#make the computer randomly select the features
for i in range(4):
    a= random.randrange(4)
    list1.append(a)


top = Tk()
CheckVar=[]
for i in range(0,16):
    CheckVar.append(IntVar())
    
r=StringVar()#get the value for right

def show_picture1():
    P1=Label(top,image=photo1).grid(row=1,column=5)
    list2[0]=0
def show_picture2():
    P2=Label(top,image=photo2).grid(row=1,column=5)
    list2[0]=1
def show_picture3():
    list2[0]=2
    P3=Label(top,image=photo3).grid(row=1,column=5)
def show_picture4():
    list2[0]=3
    P4=Label(top,image=photo4).grid(row=1,column=5)
def show_picture5():
    list2[1]=0
    P5=Label(top,image=photo5).grid(row=1,column=6)
def show_picture6():
    list2[1]=1
    P6=Label(top,image=photo6).grid(row=1,column=6)
def show_picture7():
    list2[1]=2
    P7=Label(top,image=photo7).grid(row=1,column=6)
def show_picture8():
    list2[1]=3
    P8=Label(top,image=photo8).grid(row=1,column=6)
def show_picture9():
    list2[2]=0
    P1=Label(top,image=photo9).grid(row=3,column=5)
def show_picture10():
    list2[2]=1
    P2=Label(top,image=photo10).grid(row=3,column=5)
def show_picture11():
    list2[2]=2
    P3=Label(top,image=photo11).grid(row=3,column=5)
def show_picture12():
    list2[2]=3
    P4=Label(top,image=photo12).grid(row=3,column=5)
def show_picture13():
    list2[3]=0
    P5=Label(top,image=photo13).grid(row=3,column=6)
def show_picture14():
    list2[3]=1
    P6=Label(top,image=photo14).grid(row=3,column=6)
def show_picture15():
    list2[3]=2
    P7=Label(top,image=photo15).grid(row=3,column=6)
def show_picture16():
    list2[3]=3
    P8=Label(top,image=photo16).grid(row=3,column=6)

#define the judge function
def judge():
    right=0#initial value for right ones is zero
    for i in range(4):#compare list1 with list2 to determine how many is right
        if list1[i]==list2[i]:
            right+=1
    r.set(str(right))#convert the amount into string
    Label_r=Label(textvariable=r).grid(row=1,column=9)#display on the lable how many is right
            
    
files = ["yellow.png","blue.png","green.png","red.png","yellow.gif","blue (2).png","green (2).png","red (2).png","yellow (2).png","blue (3).png","green (3).png","red (3).png","yellow (3).png","blue (4).png","green (4).png","red (4).png"]
photo = []
picture_functions = [show_picture1, show_picture2,show_picture3,show_picture4,show_picture5,show_picture6,show_picture7,show_picture8,show_picture9,show_picture10,show_picture11,show_picture12,show_picture13,show_picture14,show_picture15,show_picture16]
Buttons = []
for i in range(0,4):
    photo.append(PhotoImage(file=files[i]))
for i in range(0,4):
    Buttons.append(Button(top, image = photo[i], command=picture_functions[i]).grid(row = 1, column = i))
for i in range(4,8):
    photo.append(PhotoImage(file=files[i]))
for i in range(4,8):
    Buttons.append(Button(top, image = photo[i], command=picture_functions[i]).grid(row = 3, column = i-4))
for i in range(8,12):
    photo.append(PhotoImage(file=files[i]))
for i in range(8,12):
    Buttons.append(Button(top, image = photo[i], command=picture_functions[i]).grid(row = 5, column = i-8))
for i in range(12,16):
    photo.append(PhotoImage(file=files[i]))
for i in range(12,16):
    Buttons.append(Button(top, image = photo[i], command=picture_functions[i]).grid(row = 7, column = i-12))
   

#arrange all check buttons in a list and set their positions
C=[]
for i in range(0,4):
    C.append(Checkbutton(top, variable = CheckVar[i],height=5,width = 5).grid(row = 2, column = i))

for i in range(4,8):
    C.append(Checkbutton(top, variable = CheckVar[i],height=5,width = 5).grid(row = 4, column = i-4))

for i in range(8,12):
    C.append(Checkbutton(top, variable = CheckVar[i],height=5,width = 5).grid(row = 6, column = i-8))

for i in range(12,16):
    C.append(Checkbutton(top, variable = CheckVar[i],height=5,width = 5).grid(row = 2, column = i-12))

Judge=Button(top,text="Enter",command=judge,bg="green")#set a button to enter
Judge.grid(row= 4,column= 7)#the position of the button

judge()#let the judge function work.

    
top.mainloop()
