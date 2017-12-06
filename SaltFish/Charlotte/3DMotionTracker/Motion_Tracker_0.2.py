#######################################################################################
#3D Chromatic Motion Tracking Program
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

#Specify Libraries to Load
from PIL import *
from PIL import Image
from PIL import ImageDraw
from time import *
from math import *
#from VideoCapture import Device
import pygame
from pygame.locals import *
import opencv
from opencv import highgui


#PI:
PI = 4.0*atan(1.0)

#Specify the RGB-tuples of the Coloured Beacons:

# Beacon_1 - Dark Red
Beacon_1_Red =16*15+14 
Beacon_1_Green = 16*5+14
Beacon_1_Blue = 7*16+1
Beacon_1_Colour = "Dark Red"
Beacon_1_ArrayX = []*1000
Beacon_1_ArrayY = []*1000


# Beacon_2 - Dark Red
Beacon_2_Red = 141
Beacon_2_Green = 5
Beacon_2_Blue = 7
Beacon_2_Colour = "Dark Red"
Beacon_2_ArrayX = []*1000
Beacon_2_ArrayY = []*1000


#Colour_Tolerance - a setting to adjust the accuracy required to identify the beacons
# 0 - Must be exact
# 5 - Within 5 for R, G and B
# etc.
Colour_Tolerance = 20

#Search_Resolution: How many pixels are skipped per step in the scanning of the picture
# 1: each pixel is scanned
# 5: every 5 pixels are scanned; etc.
Search_Resolution = 1

#Num_Photos
#The number of photographs to take
Num_Photos = 10

#Specify the X and Y Sizes of the photos being taken by the camera:
Photo_Size_X = 351
Photo_Size_Y = 287

#Specify the Known Parameters of the System (Measurements in Metres)
#X_SIZE: X Dimension of the Flight Region
#Y_SIZE: Y Dimension of the Flight Region
#Z_SIZE: Z Dimension of the Flight Region
X_SIZE = 4.0
Y_SIZE = 5.0
Z_SIZE = 2.0

#Specify the Camera Parameters:
#Camera Prism Angle - X, Y - Specifies the Angle of the Prism of the Field of View of the Camera
#(In Degrees)
#This paramater must be accurately measured for each camera used with the program.
#X: From the Centre of the Field of View to the Edges in the X Direction
#Y: From the Centre of the Field of View to the Edges in the Y Direction
Camera_Prism_Angle_X = 38.0
Camera_Prism_Angle_Y = 37.0

#Calculate the Distance from the bound of the flight region based on the camera angle:
#X_Distance is used if the Camera is incident upon the flight region
#so that the camera's X coordinate corresponds with the region's X
#Y_Distance is used if the Camera is incident upon the flight region
#so that the camera's Y coordinate corresponds with the region's Y
X_Distance_X = (X_SIZE / 2.0) / tan(Camera_Prism_Angle_X * PI / 180.0)
X_Distance_Y = (Z_SIZE / 2.0) / tan(Camera_Prism_Angle_Y * PI / 180.0)
#Select the greater distance to ensure that the entire flight region is within the field of view of the camera
X_Distance = X_Distance_X
if X_Distance_Y > X_Distance_X:
        X_Distance = X_Distance_Y
print "If you are placing the camera incident upon the X-Side, please centre it ", X_Distance, " metres from"
print "the boundary of the flight region at a height of ", Z_SIZE / 2.0, " metres."

Y_Distance_X = (Y_SIZE / 2.0) / tan(Camera_Prism_Angle_X * PI / 180.0)
Y_Distance_Y = (Z_SIZE / 2.0) / tan(Camera_Prism_Angle_Y * PI / 180.0)
#Select the greater distance to ensure that the entire flight region is within the field of view of the camera
Y_Distance = Y_Distance_X
if Y_Distance_Y > Y_Distance_X:
        Y_Distance = Y_Distance_Y
print "If you are placing the camera incident upon the Y-Side, please centre it ", Y_Distance, " metres from"
print "the boundary of the flight region at a height of ", Z_SIZE / 2.0, " metres."

#Initialize the program
#The final version of the program will have a network connection protocol at this point so as to synchronize the two cameras
raw_input("Please hit any key to initiate the tracking program")



#Initialize the Camera
cam = highgui.cvCreateCameraCapture(0)

count = 0
while count < Num_Photos:
        filename = 'icamtest'+str(count)+'.jpg'
	GetFrame = highgui.cvQueryFrame(cam)
	highgui.cvSaveImage(filename,GetFrame)

        #cam.saveSnapshot(filename)
        #print time(), "Picture ", count, " taken."
        
        im = Image.open(filename)
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
        
        while cx < Photo_Size_X:
                cy = 1
                while cy < Photo_Size_Y:
                        
                        if abs(pix[cx,cy][0] - Beacon_1_Red) <= Colour_Tolerance and abs(pix[cx,cy][1] - Beacon_1_Green) <= Colour_Tolerance and abs(pix[cx,cy][2] - Beacon_1_Blue)<= Colour_Tolerance:
                                print pix[cx,cy], cx, cy, Beacon_1_Colour
                                Beacon_1_X += cx
                                Beacon_1_Y += cy
                                Beacon_1_Count += 1.0
                                #Beacon_1_ArrayX[count] = cx
                                #Beacon_1_ArrayY[count] = cy
                        if abs(pix[cx,cy][0] - Beacon_2_Red) <= Colour_Tolerance and abs(pix[cx,cy][1] - Beacon_2_Green) <= Colour_Tolerance and abs(pix[cx,cy][2] - Beacon_2_Blue)<= Colour_Tolerance:
                                print pix[cx,cy], cx, cy, Beacon_2_Colour
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
                print Beacon_1_Colour, " beacon coordinates... (",int(Beacon_1_X/Beacon_1_Count),",",int(Beacon_1_Y/Beacon_1_Count),")"
        else:
                print Beacon_1_Colour, "beacon not found"
        if Beacon_2_Count > 0:
                print Beacon_2_Colour, " beacon coordinates... (",int(Beacon_2_X/Beacon_2_Count),",",int(Beacon_2_Y/Beacon_2_Count),")"
        else:
                print Beacon_2_Colour, " beacon not found"
        print Beacon_1_Count, Beacon_2_Count, "Beacon Counts"
        count +=1
