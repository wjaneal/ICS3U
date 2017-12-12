from tkinter import *
import tkinter
import random

list2=[4,4,4,4]
list1=[]
time=0
for i in range(4):
    a= random.randrange(4)
    list1.append(a)


top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()
CheckVar10 = IntVar()
CheckVar11 = IntVar()
CheckVar12 = IntVar()
CheckVar13 = IntVar()
CheckVar14 = IntVar()
CheckVar15 = IntVar()
CheckVar16 = IntVar()
r=StringVar()
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
def judge():
    right=0
    for i in range(4):
        if list1[i]==list2[i]:
            right+=1
    r.set(str(right))
    Label_r=Label(textvariable=r).grid(row=1,column=9)
            
    
photo1 = PhotoImage(file="yellow.png")
Button1 = Button(top, image = photo1, command=show_picture1).grid(row = 1, column = 0)
photo2 = PhotoImage(file="blue.png")
Button2 = Button(top, image = photo2, command=show_picture2).grid(row = 1, column = 1)
photo3 = PhotoImage(file="green.png")
Button3 = Button(top, image = photo3, command=show_picture3).grid(row = 1, column = 2)
photo4 = PhotoImage(file="red.png")
Button4 = Button(top, image = photo4, command=show_picture4).grid(row = 1, column = 3)
photo5 = PhotoImage(file="yellow.gif")
Button5 = Button(top, image = photo5, command=show_picture5).grid(row = 3, column = 0)
photo6 = PhotoImage(file="blue (2).png")
Button6 = Button(top, image = photo6, command=show_picture6).grid(row = 3, column = 1)
photo7 = PhotoImage(file="green (2).png")
Button7 = Button(top, image = photo7, command=show_picture7).grid(row = 3, column = 2)
photo8 = PhotoImage(file="red (2).png")
Button8 = Button(top, image = photo8, command=show_picture8).grid(row = 3, column = 3)
photo9 = PhotoImage(file="yellow (2).png")
Button9 = Button(top, image = photo9, command=show_picture9).grid(row = 5, column = 0)
photo10 = PhotoImage(file="blue (3).png")
Button10 = Button(top, image = photo10, command=show_picture10).grid(row = 5, column = 1)
photo11 = PhotoImage(file="green (3).png")
Button11 = Button(top, image = photo11, command=show_picture11).grid(row = 5, column = 2)
photo12 = PhotoImage(file="red (3).png")
Button12 = Button(top, image = photo12, command=show_picture12).grid(row = 5, column = 3)
photo13 = PhotoImage(file="yellow (3).png")
Button13 = Button(top, image = photo13, command=show_picture13).grid(row = 7, column = 0)
photo14 = PhotoImage(file="blue (4).png")
Button14 = Button(top, image = photo14, command=show_picture14).grid(row = 7, column = 1)
photo15 = PhotoImage(file="green (4).png")
Button15 = Button(top, image = photo15, command=show_picture15).grid(row = 7, column = 2)
photo16 = PhotoImage(file="red (4).png")
Button16 = Button(top, image = photo16, command=show_picture16).grid(row = 7, column = 3)



C1 = Checkbutton(top, variable = CheckVar1, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 2, column = 0)
C2 = Checkbutton(top, variable = CheckVar2, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 2, column = 1)
C3 = Checkbutton(top, variable = CheckVar3, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 2, column = 2)
C4 = Checkbutton(top, variable = CheckVar4, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 2, column = 3)
C5 = Checkbutton(top, variable = CheckVar5, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 4, column = 0)
C6 = Checkbutton(top, variable = CheckVar6, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 4, column = 1)
C7 = Checkbutton(top, variable = CheckVar7, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 4, column = 2)
C8 = Checkbutton(top, variable = CheckVar8, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 4, column = 3)
C9 = Checkbutton(top, variable = CheckVar9, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 6, column = 0)
C10 = Checkbutton(top, variable = CheckVar10, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 6, column = 1)
C11 = Checkbutton(top, variable = CheckVar11, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 6, column = 2)
C12 = Checkbutton(top, variable = CheckVar12, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 6, column = 3)
C13 = Checkbutton(top, variable = CheckVar13, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 8, column = 0)
C14 = Checkbutton(top, variable = CheckVar14, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 8, column = 1)
C15 = Checkbutton(top, variable = CheckVar15, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 8, column = 2)
C16 = Checkbutton(top, variable = CheckVar16, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row = 8, column = 3)

Judge=Button(top,text="Enter",command=judge,bg="green")
Judge.grid(row= 4,column= 7)

judge()

    
top.mainloop()
