#!/usr/bin/env pythonju
#######################################################################################
#3D Chromatic Motion Tracking Program  - Server - v 1.0 - November, 2011
#Algorithm Description:
#(1) Locate Starting Position of Chromatic Tracking Targets
#(2) Specify Maximum Anticipated Movement Based on Size of Region and
#Known Motion Parameters
#(3) Loop: Take Picture; Open Picture File; Locate to Centre of Search Area Based on
#Last Known Position and Last Known Velocity Vector; Specify Search Region
#Dimensions Based on Anticipated Upper Bounds of Possible Displacements
#       Inner Loop:     Scan Search Region
#               Accumulate and Average Coordinates of Chromatic Targets Located
#Output Frame#, Time, Estimated Coordinates of Search Targets.
#########################################################################################
###With thanks to ... at BYU for the Socket programming components
#Import video / webcam libraries
import os, sys
from PIL import *
from PIL import Image
from PIL import ImageDraw
from time import *
from math import *
import pygame
from pygame.locals import *


#from VideoCapture import Device
#from opencv import cv
#import cv.highgui as highgui
import cv
#from cv import highgui

#from cv import Device

import pickle

#Import libraries for networking
import select
import socket
from string import * #The data will be sent as a string and parsed into numbers

networking = 0
if networking:
    #Specify networking parameters
    host = 'localhost' # Edited this to be 'localhost' from '', should be a good multi-use host name -Gray
    port = 50000
    backlog = 5
    size = 1024 # Edited this to be 1024 from 10240 -Gray
    #Initialize the server:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(backlog)
    #sys.stdin was removed from the following input list
    #because it is on by default, apparently, in windows.
    input = [server]
    running = 1
    print "Server working"
count = 0
 #Prepare Pickling of Output Data:
output_file = open('testdata.dat','wb')


#PI:
PI = 4.0*atan(1.0)
#Specify the RGB-tuples of the Coloured Beacons:
# Beacon_1 - Red

#RED - 0-255
#GREEN 0-255
#BLUE  0-255

Beacon_1_Red = 124
Beacon_1_Green = 55
Beacon_1_Blue = 58
Beacon_1_Colour = "Red - Magnet"
B1X = [0]*1000
B1Y = [0]*1000
#Define Received Data Arrays
RData1X = [0]*1000
RData1Y = [0]*1000
RData2X = [0]*1000
RData2Y = [0]*1000
# Beacon_2 - Red
Beacon_2_Red = 40
Beacon_2_Green = 56
Beacon_2_Blue = 116
Beacon_2_Colour = "Blue"
B2X = [0]*1000
B2Y = [0]*1000
#Colour_Tolerance - a setting to adjust the accuracy required to identify the beacons
# 0 - Must be exact
# 5 - Within 5 for R, G and B
 # etc.
Colour_Tolerance = 10
#Search_Resolution: How many pixels are skipped per step in the scanning of the picture
# 1: each pixel is scanned
# 5: every 5 pixels are scanned; etc.
Search_Resolution = 4
#Num_Photos
#The number of photographs to take
Num_Photos = 10
#Specify the X and Y Sizes of the photos being taken by the camera:
Photo_Size_X_C1 = 639
Photo_Size_Y_C1 = 479
Photo_Size_X_C2 = 639
Photo_Size_Y_C2 = 479
#Specify the Camera Parameters:

#Camera Prism Angle - X, Y - Specifies the Angle of the Prism of the Field of View of the Camera
#(In Degrees)
#This paramater must be accurately measured for each camera used with the program.
#X: From the Centre of the Field of View to the Edges in the X Direction
#Y: From the Centre of the Field of View to the Edges in the Y Direction
#Distance of camera to wall = 1.15m (April 22, 2009)
#Horizontal Size = 1.015m
#Vertical Size = 0.63m
#Input the camera parameters here:
C1_TX = atan(1.015/(1.15*2))
C1_TZ = atan(0.63/(1.15*2))
C2_TY = atan(1.207/(1.15*2))
C2_TZ = atan(0.889/(1.15*2))
#Computer 1:
Y_Distance = 1.5
   #Computer 2:
X_Distance = 1.2 
X_SIZE = 2*abs((X_Distance*tan(C1_TX)*tan(C2_TY)-Y_Distance)/(1/tan(C1_TX)-tan(C2_TY)))
#Calculate the dimensions of the visible region based
#on the distance of the camera
#X_SIZE = Y_Distance*tan(C1_TX * PI / 180.0)*2
Y_SIZE = 2*abs(-tan(C2_TY)*X_SIZE/2-(X_Distance*tan(C2_TY)))
# Y_SIZE is taken from camera 2
Z_SIZE = 2*(X_Distance)*tan(C2_TZ)
Z_SIZE1 = 2*(Y_Distance)*tan(C1_TZ)
if Z_SIZE1 < Z_SIZE:
    Z_SIZE = Z_SIZE1
print X_SIZE, Y_SIZE, Z_SIZE

def Locate_Object(M,N,P,R):
    t = P[0]/((M[2]*N[0])/(N[2])-M[0]+P[0])
    s = t*M[2]/N[2]
    #print s, "s"
    Q = [0.0]*3
    Q[0] = P[0]+t*(M[0]-P[0])
    Q[1] = t*M[1]
    Q[2] = t*M[2]
    return Q
#Convert Pixels to Metres:  Determine the coordinates in metres
#based on the number of pixels in the x and y direction
#and the dimensions of the flight region
def pix_to_metres_x(px, size_x, A):
    return px*(2*A)/size_x-A
def pix_to_metres_y(py, size_y, C):
    return -py*(2*C)/size_y+C        
#Initialize the program
#The final version of the program will have a network connection protocol at this point so as to synchronize the two cameras
raw_input("Please hit any key to initiate the tracking program")
#Initialize the Camera
#cam = Device()
#cam =  cvCreateCameraCapture(0)
cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
#for i in range(0,3):
#	cam = cv.CaptureFromCAM(i)
#	if cam: break
cam1 = cv.CaptureFromCAM(1)
cam2 = cv.CaptureFromCAM(2)

count = 0
while count < Num_Photos:
    if networking <> 0:
        #Get the server running:
        
        inputready,outputready,exceptready = select.select(input,[],[],1000)        
        for s in inputready:
            print count, " loops"
            if s == server:
                # handle the server socket
                client, address = server.accept()
                input.append(client)
                print "Server received connection"
            elif s == sys.stdin:
                # handle standard input
                print "Received junk"
                junk = sys.stdin.readline()
                running = 0
            else:
                # handle all other sockets
                print "Received something....processing"
                data1 = s.recv(size)
                ReceivedDataXY = split(data1,"*")  #Split the incoming data in 2
                                               #Use "*" as a separator
                #To do: activate the other two data points
                RData1X[count] = eval(ReceivedDataXY[0])
                RData1Y[count] = eval(ReceivedDataXY[1])
                print "First X-Y Coordinates Received: ", RData1X[count], RData1Y[count]
                RData2X[count] = eval(ReceivedDataXY[2])
                RData2Y[count] = eval(ReceivedDataXY[3])
                print "Second X-Y Coordinates Received: ", RData1X[count], RData1Y[count]
            #Take a photo here:
#########################################        
    filename1 = './testphotos/test'+str(count)+'.1.jpg'
    filename2 = './testphotos/test'+str(count)+'.2.jpg'

    GetFrame1 = cv.QueryFrame(cam1)
    GetFrame2 = cv.QueryFrame(cam2)


    cv.SaveImage(filename1, GetFrame1)
    cv.SaveImage(filename2, GetFrame2)
    print time(), "Picture ", count, " taken."
    '''
    im = Image.open(filename1)
    pix = im.load()
            # write to stdout
            #The following variables are used to average the X-Y coordinates of the beacons found.
    Beacon_1_X = 0.0
    Beacon_1_Y = 0.0
    Beacon_1_Count = 0.0
    Beacon_2_X = 0.0
    Beacon_2_Y = 0.0
    Beacon_2_Count = 0.0
    #
    cx = 1
    #At this point, efficiencies may be gained by implementing an algorithm to
    #reduce the search region
    #This must be used only if there is a high chance of beacon identification...
    while cx < Photo_Size_X_C1:
        cy = 1
        while cy < Photo_Size_Y_C1:
            if abs(pix[cx,cy][0] - Beacon_1_Red) <= Colour_Tolerance and abs(pix[cx,cy][1] - Beacon_1_Green) <= Colour_Tolerance and abs(pix[cx,cy][2] - Beacon_1_Blue)<= Colour_Tolerance:
                #print pix[cx,cy], cx, cy, Beacon_1_Colour
                Beacon_1_X += cx
                Beacon_1_Y += cy
                Beacon_1_Count += 1.0
                #Beacon_1_ArrayX[count] = cx
                #Beacon_1_ArrayY[count] = cy
            if abs(pix[cx,cy][0] - Beacon_2_Red) <= Colour_Tolerance and abs(pix[cx,cy][1] - Beacon_2_Green) <= Colour_Tolerance and abs(pix[cx,cy][2] - Beacon_2_Blue)<= Colour_Tolerance:
                #print pix[cx,cy], cx, cy, Beacon_2_Colour
                Beacon_2_X += cx
                Beacon_2_Y += cy
                Beacon_2_Count += 1.0
                #Beacon_2_ArrayX[count] = cx
                #Beacon_2_ArrayY[count] = cy
            cy += Search_Resolution
        cx += Search_Resolution
        print "Picture ", count, "has been analyzed:"
        print "Current Time: ", time()
        if Beacon_1_Count > 0:
            print count
            B1X[count] = pix_to_metres_x(int(Beacon_1_X/Beacon_1_Count),Photo_Size_X_C1,X_SIZE)
            B1Y[count] = pix_to_metres_y(int(Beacon_1_Y/Beacon_1_Count),Photo_Size_Y_C1,Y_SIZE)
            print Beacon_1_Colour, " beacon coordinates... (",B1X[count],",",B1Y[count],")"
        else:
            print Beacon_1_Colour, "beacon not found"
        if Beacon_2_Count > 0:
            B2X[count] = pix_to_metres_x(int(Beacon_2_X/Beacon_2_Count),Photo_Size_X_C1,X_SIZE)
            B2Y[count] = pix_to_metres_y(int(Beacon_2_Y/Beacon_2_Count),Photo_Size_Y_C1,Y_SIZE)      
            print Beacon_2_Colour, " beacon coordinates... (",B2X[count],",",B2Y[count],")"
        else:
            print Beacon_2_Colour, " beacon not found"
            print Beacon_1_Count, Beacon_2_Count, "Beacon Counts"
#########################################
        if networking <> 0:
            s.send("Hello - sending data: "+data1)
            #The following lines were commented out to get the server working
            #Changed May 15, 2009
        if networking <> 0:
            client.close()
            #input.remove(s)
    '''
    count +=1
pickle.dump(B1X, output_file)
pickle.dump(B1Y, output_file)
pickle.dump(B2X, output_file)
pickle.dump(B2Y, output_file)
#pickle.dump(RData1X, output_file)
#pickle.dump(RData1Y, output_file)
#pickle.dump(RData2X, output_file)
#pickle.dump(RData2Y, output_file)

output_file.close()
del(cam)
sys.exit(0)
