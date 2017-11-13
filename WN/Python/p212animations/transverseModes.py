#!/usr/bin/python2.2

from visual import *
import math

scene.title = 'Beads on a String : Transverse Modes'
scene.autoscale=0
range=6.1
scene.range=(range,range,range)


k = 10   # To/l
l = 4    # Nominal string length

Ap = 0.1
Am = 0.15
wp = sqrt(3*k)
wm = sqrt(k)

# Offsets of the three strings
oa = vector(0,3,0)
ob = vector(0,0,0)
oc = vector(0,-3,0)

# Initial positions of the beads
r10 = vector(-l/2, Ap,0) + oa
r20 = vector( l/2, -Ap,0) + oa
r30 = vector(-l/2, Am,0) + ob
r40 = vector(l/2, -Am,0) + ob
r50 = vector(-l/2,Ap+Am,0) + oc
r60 = vector(l/2,Am-Ap,0) + oc

# Display the beads in their initial states.
m1 = sphere(pos    = r10,
            radius = 0.2,
            color  = color.blue)
m2 = sphere(pos    = r20,
            radius = 0.2,
            color  = color.blue)
m3 = sphere(pos    = r30,
            radius = 0.2,
            color  = color.red)
m4 = sphere(pos    = r40,
            radius = 0.2,
            color  = color.red)
m5 = sphere(pos    = r50,
            radius = 0.2,
            color  = color.magenta)
m6 = sphere(pos    = r60,
            radius = 0.2,
            color  = color.magenta)

# Display the strings in their initial states.
stringa1 = cylinder(pos=(vector(-3*l/2,0,0)+oa),
                    axis=(m1.pos-(vector(-3*l/2,0,0)+oa)), radius=0.02)
stringa2 = cylinder(pos=m1.pos,
                    axis=(m2.pos-m1.pos), radius=0.02)
stringa3 = cylinder(pos=m2.pos,
                    axis=(vector(3*l/2,0,0)+oa-m2.pos), radius=0.02)

stringb1 = cylinder(pos=(vector(-3*l/2,0,0)+ob),
                    axis=(m3.pos-(vector(-3*l/2,0,0)+ob)), radius=0.02)
stringb2 = cylinder(pos=m3.pos,
                    axis=(m4.pos-m3.pos), radius=0.02)
stringb3 = cylinder(pos=m4.pos,
                    axis=(vector(3*l/2,0,0)+ob-m4.pos), radius=0.02)

stringc1 = cylinder(pos=(vector(-3*l/2,0,0)+oc),
                    axis=(m5.pos-(vector(-3*l/2,0,0)+oc)), radius=0.02)
stringc2 = cylinder(pos=m5.pos,
                    axis=(m6.pos-m5.pos), radius=0.02)
stringc3 = cylinder(pos=m6.pos,
                    axis=(vector(3*l/2,0,0)+oc-m6.pos), radius=0.02)

dt = 0.01      # Time increment

n=0
while 1:
    rate(100)  # Increments per second

    t = n*dt   # Advance the clock.

    # Update bead positions.
    m1.pos.y = Ap*cos(wp*t) + oa.y
    m2.pos.y = -Ap*cos(wp*t) + oa.y

    m3.pos.y = Am*cos(wm*t) + ob.y
    m4.pos.y = Am*cos(wm*t) + ob.y

    m5.pos.y = Ap*cos(wp*t) + Am*cos(wm*t) + oc.y
    m6.pos.y = -Ap*cos(wp*t) + Am*cos(wm*t) + oc.y

    # Update the positions and orientations of the strings.
    stringa1.axis = m1.pos-(vector(-3*l/2,0,0)+oa)
    stringa2.pos  = m1.pos
    stringa2.axis = m2.pos-m1.pos
    stringa3.pos  = m2.pos
    stringa3.axis = vector(3*l/2,0,0)+oa-m2.pos

    stringb1.axis = m3.pos-(vector(-3*l/2,0,0)+ob)
    stringb2.pos  = m3.pos
    stringb2.axis = m4.pos-m3.pos
    stringb3.pos  = m4.pos
    stringb3.axis = vector(3*l/2,0,0)+ob-m4.pos

    stringc1.axis = m5.pos-(vector(-3*l/2,0,0)+oc)
    stringc2.pos  = m5.pos
    stringc2.axis = m6.pos-m5.pos
    stringc3.pos  = m6.pos
    stringc3.axis = vector(3*l/2,0,0)+oc-m6.pos

    n = n+1    # Advance the clock counter
