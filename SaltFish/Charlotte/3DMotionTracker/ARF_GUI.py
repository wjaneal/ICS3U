# GUI for Automated RC Flight Program

from Tkinter import *
root = Tk()

def hello():
    print "hello!"




menubar = Menu(root)

#File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Flight Plan", command=hello, underline = 12)

filemenu.add_command(label="Load Flight Data", command=hello, underline = 12)
filemenu.add_command(label="Save Flight Data", command=hello, underline = 0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit, underline = 1)
menubar.add_cascade(label="File", menu=filemenu, underline = 0)

# create more pulldown menus
configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Camera", command=hello, underline = 0)
configmenu.add_command(label="Server / Client", command=hello, underline = 0)
configmenu.add_command(label="Arduino", command=hello, underline = 0)
configmenu.add_command(label="Flight Parameters", command=hello, underline = 0)
configmenu.add_command(label="Colour Settings", command=hello, underline = 1)
configmenu.add_command(label="Image Processing Settings", command=hello, underline = 0)
menubar.add_cascade(label="Configure", menu=configmenu, underline = 0)

# Test Menu
testmenu = Menu(menubar, tearoff=0)
testmenu.add_command(label="Camera", command=hello, underline = 0)
testmenu.add_command(label="Network", command=hello, underline = 0)
testmenu.add_command(label="Arduino", command=hello, underline = 0)
menubar.add_cascade(label="Test", menu=testmenu, underline = 0)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello, underline = 0)
menubar.add_cascade(label="Help", menu=helpmenu, underline = 0)

# display the menu
root.config(menu=menubar)
root.title("Automated RC Flight Program")

mainloop()




