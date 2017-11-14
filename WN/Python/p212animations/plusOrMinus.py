#!/usr/bin/python2.2

from visual import *
from planeWave import *
import math

H    = 700         # Scene height [pixels]
W    = 500         # Scene width  [pixels]
scene.title = 'Plane Wave'
scene.height = H
scene.width = W
scene.autoscale = 0
scene.range = vector(55, 55, 55)

Sep = 25

fr = frame()

w1 = planeWave(fr=fr,
               f=100,
               r = (-1.5*Sep,0, 0),
               graphRadius = 0.2)
w1Label = label(frame   = fr,
                pos     =  (-2.0*Sep, 0, 0),
                opacity = 0,
                text    = '(kx - wt)')

w2 = planeWave(fr=fr,
               f=100,
               r = (-0.5*Sep, 0, 0),
               graphRadius = 0.2,
               k = -pi/4.0)
w2Label = label(frame   = fr,
                pos     =  (-1.0*Sep, 0, 0),
                opacity = 0,
                text    = '(-kx - wt)')

w3 = planeWave(fr=fr,
               f=100,
               r = ( 0.5*Sep, 0, 0),
               graphRadius = 0.2,
               omega = -pi)
w3Label = label(frame   = fr,
                pos     =  (0, 0, 0),
                opacity = 0,
                text    = '(kx + wt)')

w4 = planeWave(fr=fr,
               f=100,
               r = ( 1.5*Sep, 0, 0),
               graphRadius = 0.2,
               k = -pi/4.0,
               omega = -pi)
w4Label = label(frame   = fr,
                pos     =  (Sep, 0, 0),
                opacity = 0,
                text    = '(-kx + wt)')

fr.rotate(angle=-pi/2.0, axis = (0,0,1))

while 1:
    w1.step()
    w2.step()
    w3.step()
    w4.step()
