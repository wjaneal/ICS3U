from Tkinter import *
import random
import pickle
from math import *

root = Tk()

#Import pickled data....
data_file_1 = open('testdata.dat','rb')
data_1 = pickle.load(data_file_1)
data_2 = pickle.load(data_file_1)
print data_1
######

def drawpixel(canv,x,y,xlast,ylast):
    # changed this to return the ID
    
        canv.create_line(x,y,xlast,ylast)
    #canv.create_oval(x,y,x,y)

def movecircle(canv, cir):
    a = int(random.random()*21-10)
    b = int(random.random()*21-10)
    canv.move(cir,a,b)

def callback(event):
    count = 0
    while count < 1000:
        theta = (random.random()*300*10000*atan(1)/300)
        r = (60*sin(theta/10))*3
        x = data1[count]
        y = count
        drawpixel(canvas, x,y)
        count +=1

def transcoord(x1,x2,X1,X2,x):
    if x2-x1 <> 0 :
        return (X2-X1)*(x-x1)/(x2-x1)+X1
    else:
        print "Error - no range given"
        return 0


##This function determines the 3-D coordinates of the object based on
##the 2-D coordinates provided by each camera
def Locate_Object(M,N,P,R):
    t = P[0]/((M[2]*N[0])/(N[2])-M[0]+P[0])
    s = t*M[2]/N[2]
    #print s, "s"
    Q = [0.0]*3
    Q[0] = P[0]+t*(M[0]-P[0])
    Q[1] = t*M[1]
    Q[2] = t*M[2]
    return Q

    
canvas = Canvas(width=600, height=600, bg='white')
canvas.bind("<Button-1>", callback)
canvas.pack(expand=YES, fill=BOTH)
root.title("3D Flight Path Display Program")

text = canvas.create_text(100,10, text="          Click the mouse button to display flight path data")

#i'd like to recalculate these coordinates every frame


xaxis_X1 = transcoord(-3,3,100,500,-3)
xaxis_X2 = transcoord(-3,3,100,500,3)
xaxis_Y1 = transcoord(-1,5,500,100,0)
xaxis_Y2 = transcoord(-1,5,500,100,0)
#canvas.create_line(xaxis_X1, xaxis_Y1, xaxis_X2, xaxis_Y2)

yaxis_X1 = transcoord(-3,3,100,500,0)
yaxis_X2 = transcoord(-3,3,100,500,0)
yaxis_Y1 = transcoord(-1,5,500,100,-2)
yaxis_Y2 = transcoord(-1,5,500,100,6)
#canvas.create_line(yaxis_X1, yaxis_Y1, yaxis_X2, yaxis_Y2)

xmin = 0
xmax = 5
ymin = -3
ymax = 3
x = xmin
XLast = 0
YLast = 0
while x < xmax:
    #y = x*x
    #Apply X and Y data here////
    x1 = data_1[int(x*50)]
    y = data_2[int(x*50)]
    X = transcoord(xmin,xmax,100,500,x1)
    Y = transcoord(ymin,ymax,500,100,y)
    if abs(x1) > 0 and abs(y) > 0:
        drawpixel(canvas,X,Y,XLast,YLast)
    XLast = X
    YLast = Y
    #drawpixel(canvas,X,Y+20)
    x+=0.01

    


    

root.mainloop()
