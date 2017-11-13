#!/usr/bin/python2.2

from visual import *
from planeWave import *
import math

H    = 600         # Scene height [pixels]
W    = 400         # Scene width  [pixels]

scene.title = 'Quantum Beats'
scene.height = H
scene.width = W
scene.autoscale = 0
scene.range = vector(60, 60, 60)

k1     = 0.8*pi/4.0
omega1 = k1**2/2.0
k2     = pi/4.0
omega2 = k2**2/2.0

s = superposition()
w1 = planeWave(r           = (0,-25,0),
               omega       = omega1,
               k           = k1,
               nGraph      = 200,
               graphLength = 80,
               graphColor  = color.blue,
               pointColor  = color.blue,
               dt          = 0.1,
               f           = 60)
w2 = planeWave(r           = (0,-25,0),
               omega       = omega2,
               k           = k2,
               nGraph      = 200,
               graphLength = 80,
               graphColor  = color.red,
               pointColor  = color.red,
               dt          = 0.2,
               f           = 60)
s.append(w1)
s.append(w2)
while 1:
    s.step()
