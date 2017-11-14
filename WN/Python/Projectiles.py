from math import *
from vpython import *

PI = 4.0*atan(1.0)
g = 9.8
Iterations = 1200
Scale = 1
#Define Solution of a Quadratic Equation
def quadratic(a,b,c):
	Roots = [0.0]*2
	if (b*b-4*a*c >= 0):
		Roots[0] = (-b+sqrt(b*b-4*a*c))/(2*a)
		Roots[1] = (-b-sqrt(b*b-4*a*c))/(2*a)
		return Roots
	else:
		return "Error"

P = points(pos=vector(0,0,0), color=color.red)
#Get Data
print("This program takes the initial velocity, the initial height and final height and calculates the time of flight and the horizontal distance travelled")
#V = input("Please enter the magnitude of V, the initial velocity")
#Theta = input("Please enter theta, the initial angle in degrees, above the horizon (must be in the range 0 to 90)")
V = 50
Theta = 60.0
Hi = 0
Hf = 0
Vx = V*cos(Theta * PI/180)
Vy = V*sin(Theta*PI/180)
#Hi = input("Please enter Hi, the initial height")
#Hf = input("Please enter Hf, the final height")
Time_to_Max = Vy/g
Max_Height = Vy*(Time_to_Max)-(Time_to_Max)*(Time_to_Max)*0.5*g+Hi
if Hf > Max_Height:
	print ("The object will never reach the given final height")
else:
	# d = d0+v0t+(1/2)at^2
	# hf = hi + vyt-(g/2)t^2
	a = -(g/2)
	b = Vy
	c = Hi
	Roots = quadratic(a,b,c)
	if Roots == "Error":
		print ("There is no solution to the given initial conditions")
	else:
		print(Roots[0]," is the first root")
		print(Roots[1], " is the second root")

	for i in range (1, Iterations):
		t = i*Roots[1]/(Vx*Iterations)
                Dy = Hi + Vy*t-0.5*g*t**2
                #x = i*Roots[1]/Scale
                #y = Dy/Scale
		#P.append((x,y,0))
		
	

