#Spherical Fly Problem
#Copyleft 2013, William Neal
#Uses Python Visual Module to Display the path of an imaginary fly
#as determined by an equation in spherical coordinates

#Import the required modules for math and graphics:
import math
from vpython import *

#Set a scale factor to determine the time interval for each calculation:
Scale = 0.001


#Set up conversion from spherical coordinates to cartesian coordinates
def Spherical_to_Cartesian(r, theta, phi):
	x = r*sin(phi)*cos(theta)
	y = r*sin(phi)*sin(theta)
	z = r*cos(phi)
	return (x,y,z)

#Draw points to show where the fly has been:
P = points(pos=vector(0,0,0), color = color.red)
#Draw a vector to show where the fly is:
Fly = arrow(pos = vector(0.000001,0,0), axis = vector(0,0,1), shaftwidth = 0.1)
#Draw a sphere to represent the surface on which the fly flies:
ball = sphere(pos=vector(0,0,0), radius=1, opacity = 0.4)

#Calculate the path of the fly using a loop 
for t in range(1,20000):
	#Calculate the new angles based on the scale
	Phi = 3*t*Scale
	Theta = t*Scale
	#Determine the (x,y,z) Coordinates using the transformation function:
	Coords = Spherical_to_Cartesian(1.0,Theta,Phi)
	Fly.axis = vector(Coords[0],Coords[1],Coords[2])
	#Place a new point on the screen where the fly is now
	P.append((Coords[0],Coords[1],Coords[2]))
	#Adjust the rate of the loop so that the animation can be seen:
	rate(300)
	
