#!/usr/bin/python2.2

from visual import *
from planeWave import *
from math import *

H    = 600         # Scene height [pixels]
W    = 400         # Scene width  [pixels]
scene.title = 'Standing Wave'
scene.height = H
scene.width = W
scene.autoscale = 0
scene.range = vector(35, 35, 35)

s = superposition()
w1 = planeWave(k=pi/8.0,
               graphColor=color.blue,
               graphLength = 32.0,
               pointColor=color.blue)
w2 = planeWave(k=-pi/8.0,
               phi = pi,
               graphColor=color.red,
               graphLength = 32.0,
               pointColor=color.red)
s.append(w1)
s.append(w2)
while 1:
    s.step()
