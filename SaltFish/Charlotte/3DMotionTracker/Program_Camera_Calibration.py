from math import *

#Camera 1 - Along x axis
x1 = 1.5
#Camera 2 - Along y axis
y2 = 1.5
#Camera 1 Angle (Radians):
C1_TX = atan(1.015/(1.15*2))
C1_TZ = atan(0.63/(1.15*2))
#Camera 2 Angle (Radians):
C2_TY = atan(1.207/(1.15*2))
C2_TZ = atan(0.889/(1.15*2))

#Calculate the coordinates of the corner of the field of view:
print C1_TX,C2_TY
b1 = tan(C1_TX)*x1
m1 = -b1/x1
x = (y2-x1*tan(C1_TX))/(-tan(C1_TX)+1/tan(C2_TY))
y = m1*x+b1
z1 = tan(C1_TZ)*x1
z2 = tan(C2_TZ)*y2
print "z:", max(z1,z2)
print x,y, m1,b1
