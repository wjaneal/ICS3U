import tkinter

filewin = tkinter.Tk()
tkinter.Label09 = tkinter.Label(filewin, textvariable=tkinter.t09, bg="white")
tkinter.grid(row=0,coloum=9)
tkinter.Label19 = tkinter.Label(filewin, textvariable=tkinter.t19, bg="white")
tkinter.grid(row=1,coloum=9)
tkinter.command = tkinter.Button(filewin, text="Enter", command=tkinter.command, bg="green")
tkinter.command.grid(row=4,column=7)