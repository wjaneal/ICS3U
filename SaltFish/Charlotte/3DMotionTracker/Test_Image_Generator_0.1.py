


#Specify Libraries to Load
import os, sys
from PIL import *
from PIL import Image
from PIL import ImageDraw
from time import *
from math import *
from VideoCapture import Device

########################################################################


A = 2
B = 2
C = 2
D = 4
E = 4

#Set the vectors required for the calculation

#P is the Position Vector of the Coordinates of Camera 1
P = [0.0]*3
P[0] = -D

#Q is the Position Vector of the Tracked Object (x,y,z)
Q = [0.0]*3

#R is the Position Vector of the Coordinates of Camera 2
R = [0.0]*3
R[1] = -E


#M is the Position Vector of the Intersection of the x-axis
#and the side of the flight region closest to Camera 1
M = [0.0]*3
M[0] = -A

#N is the Position Vector of the Intersection of the y-axis
#and the side of the flight region closest to Camera 2
N = [0.0]*3
N[1]= -B


def Cam_1_Resolve(P,Q,M):
    PQ = [0]*3
    #print PQ, "PQ"
    count = 0
    while count < 3:
        PQ[count] = Q[count]-P[count]
        count += 1
    t = (M[0]-P[0])/PQ[0]
    #M[1] and M[2] are the x and y coordinates of Camera 1's view of the object
    M[1] = PQ[1]*t
    M[2] = PQ[2]*t

def Cam_2_Resolve(R,Q,N):
    RQ = [0]*3
    #print RQ, "RQ"
    count = 0
    while count < 3:
        RQ[count] = Q[count]-R[count]
        count += 1
    t = (N[1]-R[1])/RQ[1]
    #N[0] and N[2] are the x and y coordinates of Camera 2's view of the object
    N[0] = RQ[0]*t
    N[2] = RQ[2]*t

def Locate_Object(M,N,P,R):
    t = P[0]/((M[2]*N[0])/(N[2])-M[0]+P[0])
    s = t*M[2]/N[2]
    #print s, "s"
    Q = [0.0]*3
    Q[0] = P[0]+t*(M[0]-P[0])
    Q[1] = t*M[1]
    Q[2] = t*M[2]
    return Q


#Set the Point
Q[0] = 0.1
Q[1] = 0.2
Q[2] = 0.3


count = 0.0
#outfile = "image" + "_TEST" +".jpg"
while count < 700:
    Q[0] = 50*cos(count/20)
    Q[1] = 60*sin(count/20)
    Q[2] = 40*sin(count/30)
    print count
    outfile = "image" + str(count) +".jpg"
    
    #im = Image.open("image_TEST.jpg")
    im = Image.open("baseimage.jpg")
    draw = ImageDraw.Draw(im)
    Cam_1_Resolve(P,Q,M)
    Cam_2_Resolve(R,Q,N) 
    x1 = 200+M[1]
    y1 = 200+M[2]
    print M, count
    x2 = x1+10
    y2 = y1+10
    draw.ellipse([x1,y1,x2,y2], fill = 228)
    del draw
    count += 1.0
    im.save(outfile, "JPEG")




#Resolve the Point with the two cameras

Cam_2_Resolve(R,Q,N)
Q = Locate_Object(M,N,P,R)




#Display the results
print M
print N
print Q
