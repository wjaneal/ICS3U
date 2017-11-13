#Orbit calculation program - Universal Gravitation
#By How much was last week's large asteroid 
#deflected by the Earth? (Change in Angle)

#Try changing the default values of G, v, R to get interesting effects
#Assignment:  
#(1)
#(a)Change each of the values by +-1% and note any effects
#(b)Change each of the values by +-10% and note any effects
#(c)Change each of the values by +-50% and note any effects

#(2) 
#(a)Add 0.01% to G each time - note any effects
#(b)Subtract 0.01% from G each time - note any effects

#(3)
#Creative orbit competition - find a combination of the above changes that makes the best possible



import tkinter as Tkinter
from math import *
root = Tkinter.Tk()

#Epochs
epochs = 550000


#PI
PI = 4*atan(1)
#Time Increment
dt = 360

#Solar System Data:
G = 6.67*10**(-11)# *1.01#Gravity
M = 5.98*10**(24)
#M = 4.867*10**24
MS = 1.99*10**(30)

#Circumference of Earth Orbit
C = 2*PI*1.49*10**(11)
#C = 2*PI*1.0802*10**9
#1 Year in seconds:
T = 365*24.0*3600.0
#Speed of Earth Orbit:
v = C/T # Speed

#Initial Position Data
#Sun:
X = 0.0
Y = 0.0
#Earth
x = 1.49*10**(11) #R
x = 1.0802*10**9
y = 0

#Initial Velocity Data
vx = 0.0
vy = v #Original

#Plot Coordinates - centre
XCentre = 150
YCentre = 150

def GravitationalForce(G,M1,M2,r):
        return G*M1*M2/(r**2)

def Hypotenuse(x,y):
    return sqrt(x**2+y**2)

def Angle(dx,dy):
        if dx>0:
                return atan(dy/dx)
        else:
                return PI+atan(dy/dx)

        



def f(x):
    return 20+10*sin(x*10000)



def pixel(image, pos, color):
    """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
    r,g,b = color
    x,y = pos
    image.put("#%02x%02x%02x" % (r,g,b), (x, y))

photo = Tkinter.PhotoImage(width=320, height=320)

pixel(photo, (XCentre,YCentre), (0,255,255))  # One lone pixel in the middle...
for i in range(0, epochs):
 
    dx = x-X
    dy = y-Y
    #G*=1.000005
    R = Hypotenuse(dx, dy)
    F = -GravitationalForce(G, MS, M, R)
    Theta = Angle(dx,dy)
    ax = F*cos(Theta)/M
    ay = F*sin(Theta)/M
    vx += ax*dt
    vy += ay*dt
    x+=vx*dt
    y+=vy*dt
    #print (x,y)
    xc = abs(XCentre+int(x/(1.49*10**9)))
    yc = abs(YCentre+int(y/(1.49*10**9)))
    #print xc,yc
    pixel(photo, (xc,yc), (255,0,0))  # One lone pixel in the middle...
label = Tkinter.Label(root, image=photo)
label.grid()
root.mainloop()
