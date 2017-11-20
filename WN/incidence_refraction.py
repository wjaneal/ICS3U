from math import *
pi = 4*atan(1)
incidence_angles = [0.0001,10,20,30,40,50,60]
water_refraction = [0.0001,7,14,21,28,35,42]
oil_refraction = [0.0001,8,12,20,24,34,59]
water_results = []
oil_results = []
for i in range(0,len(incidence_angles)):
    water_results.append(sin(incidence_angles[i]*pi/180)/sin(water_refraction[i]*pi/180))
    oil_results.append(sin(incidence_angles[i]*pi/180)/sin(oil_refraction[i]*pi/180))
print(water_results)
print(oil_results)

