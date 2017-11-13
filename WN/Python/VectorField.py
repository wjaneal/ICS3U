#Vector Field Program 
#Copyleft 2013, William Neal
#Uses Python Visual Module to Display a Vector Field 
#as determined by an equation in spherical coordinates

#Import the required modules for math and graphics:
import math
from visual import *

#Set a scale factor to determine the time interval for each calculation:
Scale = 0.001

#Calculates and returns the magnitude of a gravitational field
#Given G, the Gravitational constant, M and r

def GravitationalField(G, M, r):
	return G*M/(r*r)

def r(x,y,z):
	return sqrt(x**2+y**2+z**2)

'''#Set up conversion from spherical coordinates to cartesian coordinates
def Spherical_to_Cartesian(r, theta, phi):
	x = r*sin(phi)*cos(theta)
	y = r*sin(phi)*sin(theta)
	z = r*cos(phi)
	return (x,y,z)
'''

#Draw points to show where the fly has been:
P = points(pos = [(0.000001,0,0)], size = 1, color = color.red)
#Draw a vector to show where the fly is:
Field = [arrow(pos = (0.000001,0,0), axis = (0,0,1), shaftwidth = 0.1, length = 1)]
#Draw a sphere to represent the surface on which the fly flies:
ball = sphere(pos=(0,0,0), radius=1, opacity = 0.4)

for x in range(-10,10):
	for y in range(-10,10):
		for z in range(-10,10):
			Field.append(arrow(pos=(x,y,z), axis = (0,0,1),shaftwidth = 0.1,length = GravitationalField(1,100,0.0011+r(x,y,z))))





