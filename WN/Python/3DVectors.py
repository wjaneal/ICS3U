from visual import *
pointer = arrow(pos=(0,2,1), axis=(5,0,0), shaftwidth=0.1)
for i in range(1,100):
	pointer.rotate(angle = pi/100, axis = 2, origin = 1)

