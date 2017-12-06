#Data processing unit for the Automated RC Flight Program
from string import *

#The separator for the data transfer between computers is '*'
A = "4.223344556*-1.344334434"


#Split the string into two parts
P = split(A,'*')
print P
PNum = [0]*2
#Convert each part to a number
PNum[0] = eval(P[0])
PNum[1] = eval(P[1])
print PNum[0]+PNum[1]

