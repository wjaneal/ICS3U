from tkinter import *
import tkinter

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
C1 = Checkbutton(top, text = "Blue", variable = CheckVar1, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 20)
C2 = Checkbutton(top, text = "Red", variable = CheckVar2, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 20)
C3 = Checkbutton(top, text = "Blue", variable = CheckVar3, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 20)
C4 = Checkbutton(top, text = "Red", variable = CheckVar4, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 20)
C5 = Checkbutton(top, text = "Blue", variable = CheckVar5, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 20)
C6 = Checkbutton(top, text = "Red", variable = CheckVar6, \
 onvalue = 1, offvalue = 0, height=5, \
 width = 20)
top.mainloop()
i
