from math import * 
from random import * 
 
pi = 4*atan(1.0) 
 
points = ((0,-11.5),(1.2,-2.1),(2.5,8.2),(3.8,16.4),(4.9,7.8),(6.4,-2.5),(7.8,-12.2),(9.0,-2.3),(10.2,8.4)) 
parameters = [0,0,0,0] 
lasttotal = 1000 
i = 0
while i < 1000000: 
    a = random()*20 
    b = random()*20 
    c = random()*10 
    d = random()*20 
    total = 0
    for q in range(0,len(points)):
        total +=(points[q][1]-(a*sin(2*pi/b*(points[q][0]-d))+c))**2
    if total < lasttotal:
        lasttotal = total
        parameters = [a,b,c,d]
    i+=1
print(parameters, lasttotal)
