#!/usr/bin/python2.2

from visual import *
from planeWave import *
import math

H    = 600         # Scene height [pixels]
W    = 400         # Scene width  [pixels]

scene.title = 'Non-dispersive Beats'
scene.height = H
scene.width = W
scene.autoscale = 0
scene.range = vector(60, 60, 60)

s = superposition()
w1 = planeWave(r=(0,-25,0),
               omega=pi,
               k=pi/4.0,
               nGraph = 200,
               graphLength=80,
               graphColor=color.blue,
               pointColor=color.blue,
               dt = 0.02,
               f=60)
w2 = planeWave(r=(0,-25,0),
               omega = 0.8*pi,
               k=0.8*pi/4.0,
               nGraph = 200,
               graphLength=80,
               graphColor=color.red,
               pointColor=color.red,
               dt = 0.02,
               f=60)
s.append(w1)
s.append(w2)
while 1:
    s.step()
