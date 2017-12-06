from tkinter import *
import tkinter

def show_picture1():
    Label(top,image=photo1).grid(row=1,column=5)
def show_picture2():
    Label(top,image=photo2).grid(row=1,column=5)
def show_picture3():
    Label(top,image=photo3).grid(row=1,column=5)
def show_picture4():
    Label(top,image=photo4).grid(row=1,column=5)
def show_picture5():
    Label(top,image=photo5).grid(row=3,column=8)
def show_picture6():
    Label(top,image=photo6).grid(row=3,column=8)    
def show_picture7():
    Label(top,image=photo7).grid(row=3,column=8)
def show_picture8():
    Label(top,image=photo8).grid(row=3,column=8)
def show_picture9():
    Label(top,image=photo9).grid(row=1,column=8)
def show_picture10():
    Label(top,image=photo10).grid(row=1,column=8)
def show_picture11():
    Label(top,image=photo11).grid(row=1,column=8)
def show_picture12():
    Label(top,image=photo12).grid(row=1,column=8)
def show_picture13():
    Label(top,image=photo13).grid(row=3,column=5)
def show_picture14():
    Label(top,image=photo14).grid(row=3,column=5)
def show_picture15():
    Label(top,image=photo15).grid(row=3,column=5)
def show_picture16():
    Label(top,image=photo16).grid(row=3,column=5)
#
def player_select():
    list2=[[0 for x in range]for y in range]
    
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

photo1 = PhotoImage(file="yellow.png",)
Button(top,image=photo1,command=show_picture1).grid(row=1, column=0 )
photo2 = PhotoImage(file="blue.png",)
Button(top,image=photo2,command=show_picture2).grid(row=1, column=1)
photo3 = PhotoImage(file="green.png",)
Button(top,image=photo3,command=show_picture3).grid(row=1, column=2)
photo4 = PhotoImage(file="red.png",)
Button(top,image=photo4,command=show_picture4).grid(row=1, column=3)
photo5 = PhotoImage(file="yellow.gif",)
Button(top,image=photo5,command=show_picture5).grid(row=3, column=0)
photo6 = PhotoImage(file="blue (2).png",)
Button(top,image=photo6,command=show_picture6).grid(row=3, column=1)
photo7 = PhotoImage(file="red (2).png",)
Button(top,image=photo7,command=show_picture7).grid(row=3, column=2)
photo8 = PhotoImage(file="green (2).png",)
Button(top,image=photo8,command=show_picture8).grid(row=3, column=3)
photo9 = PhotoImage(file="yellow (2).png",)
Button(top,image=photo9,command=show_picture9).grid(row=5, column=0 )
photo10 = PhotoImage(file="blue (3).png",)
Button(top,image=photo10,command=show_picture10).grid(row=5, column=1)
photo11 = PhotoImage(file="green (3).png",)
Button(top,image=photo11,command=show_picture11).grid(row=5, column=2)
photo12 = PhotoImage(file="red (3).png",)
Button(top,image=photo12,command=show_picture12).grid(row=5, column=3)
photo13 = PhotoImage(file="yellow (3).png",)
Button(top,image=photo13,command=show_picture13).grid(row=7, column=0)
photo14 = PhotoImage(file="blue (4).png",)
Button(top,image=photo14,command=show_picture14).grid(row=7, column=1)
photo15 = PhotoImage(file="red (4).png",)
Button(top,image=photo15,command=show_picture15).grid(row=7, column=2)
photo16 = PhotoImage(file="green (4).png",)
Button(top,image=photo16,command=show_picture16).grid(row=7, column=3)
#
check=PhotoImage(file="............",)
Button(top,image=check,command=player_select).grid(row=???,column=?????)
#
C1 = Checkbutton(top,  variable = CheckVar1, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=2, column=0)
C2 = Checkbutton(top,  variable = CheckVar2, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=2, column=1)
C3 = Checkbutton(top,  variable = CheckVar3, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=2, column=2)
C4 = Checkbutton(top,  variable = CheckVar4, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=2, column=3)
C5 = Checkbutton(top, variable = CheckVar5, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=4, column=0)
C6 = Checkbutton(top, variable = CheckVar6, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=4, column=1)
C7 = Checkbutton(top, variable = CheckVar7, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=4, column=2)
C8 = Checkbutton(top, variable = CheckVar8, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=4, column=3)
C9 = Checkbutton(top,  variable = CheckVar9, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=6, column=0)
C10 = Checkbutton(top,  variable = CheckVar10, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=6, column=1)
C11 = Checkbutton(top,  variable = CheckVar11, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=6, column=2)
C12 = Checkbutton(top,  variable = CheckVar12, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=6, column=3)
C13 = Checkbutton(top, variable = CheckVar13, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=8, column=0)
C14 = Checkbutton(top, variable = CheckVar14, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=8, column=1)
C15 = Checkbutton(top, variable = CheckVar15, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=8, column=2)
C16 = Checkbutton(top, variable = CheckVar16, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 5).grid(row=8, column=3)

top.mainloop()
