#!/usr/bin/python2.2

from visual import *
from planeWave import *
import math

H    = 600         # Scene height [pixels]
W    = 800         # Scene width  [pixels]
scene.title = 'Standing Wave'
scene.height = H
scene.width = W
scene.autoscale = 0
scene.range = vector(45, 45, 45)

s = superposition()
w1 = planeWave(k=2.5*pi/8.0,
               graphColor=color.blue,
               graphLength = 32.0,
               pointColor=color.blue)
w2 = planeWave(k=-2.5*pi/8.0,
               phi = pi,
               graphColor=color.red,
               graphLength = 32.0,
               pointColor=color.red)
w3 = planeWave(k=2.0*pi/8.0,
               graphColor=color.yellow,
               graphLength = 32.0,
               pointColor=color.yellow)
w4 = planeWave(k=-2.0*pi/8.0,
               phi = pi,
               graphColor=color.green,
               graphLength = 32.0,
               pointColor=color.green)
s.append(w1)
s.append(w2)
s.append(w3)
s.append(w4)
while 1:
    s.step(dt=0.02)
