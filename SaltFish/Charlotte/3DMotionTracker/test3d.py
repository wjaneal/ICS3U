from math import *

D = 3
E = 3
A = 1
B = 1
m2 = -1
m3 = 1
n1 = -1
n3 = 1

t = E*n3*n3/(m3*((E-B)*n3-m2*m3))
X = -D+t*(D-A)
Y = t*m2
Z = t*m3
print X,Y,Z
