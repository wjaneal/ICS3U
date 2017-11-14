#!/usr/bin/python2.2

from visual import *
import math

scene.title = 'Double Pendulum'
scene.autoscale = 0
range = 1.6
scene.range=vector(range,range,range)

g = 10                        # Acceleration due to gravity
l = 1                         # Pendulum Length
Ap = 0.05                     # Amplitude of the fast mode
Am = 0.1                      # Amplitude of the slow mode
wp = sqrt(g/l*(2+sqrt(2)))    # Frequency of the fast mode
wm = sqrt(g/l*(2-sqrt(2)))    # Frequency of the slow mode

# Offsets of the three pendulums
oa = vector(-1.0,l,0)
ob = vector(0,l,0)
oc = vector(1.0,l,0)

# Initial positions of the pendulum masses
r10 = vector(l*sin(Ap),-l*cos(Ap),0) + oa
r20 = vector(-l*sin(Ap*sqrt(2)),-l*(cos(Ap)+cos(sqrt(2)*Ap)),0) + oa
r30 = vector(l*sin(Am),-l*cos(Am),0) + ob
r40 = vector(l*sin(Am*sqrt(2)),-l*(cos(Am)+cos(sqrt(2)*Am)),0) + ob
r50 = vector(l*sin(Ap+Am),-l*cos(Ap+Am),0) + oc
r60 = vector(-l*sin((Am-Ap)*sqrt(2)),
             -l*(cos(Am-Ap)+cos(sqrt(2)*(Am-Ap))),0) + oc

# Display spheres at the pivot points.
pivota = sphere(pos=oa, radius=0.05, color=color.white)
pivotb = sphere(pos=ob, radius=0.05, color=color.white)
pivotc = sphere(pos=oc, radius=0.05, color=color.white)

# Display the pendulum masses in their initial states.
m1 = sphere(pos    = r10,
            radius = 0.05,
            color  = color.blue)
m2 = sphere(pos    = r20,
            radius = 0.05,
            color  = color.blue)
m3 = sphere(pos    = r30,
            radius = 0.05,
            color  = color.red)
m4 = sphere(pos    = r40,
            radius = 0.05,
            color  = color.red)
m5 = sphere(pos    = r50,
            radius = 0.05,
            color  = color.magenta)
m6 = sphere(pos    = r60,
            radius = 0.05,
            color  = color.magenta)

# Display the strings in their initial states.
string1 = cylinder(pos=pivota.pos, axis=(m1.pos-pivota.pos), radius=0.01)
string2 = cylinder(pos=m1.pos, axis=(m2.pos-m1.pos), radius=0.01)

string3 = cylinder(pos=pivotb.pos, axis=(m3.pos-pivotb.pos), radius=0.01)
string4 = cylinder(pos=m3.pos, axis=(m4.pos-m3.pos), radius=0.01)

string5 = cylinder(pos=pivotc.pos, axis=(m5.pos-pivotc.pos), radius=0.01)
string6 = cylinder(pos=m5.pos, axis=(m6.pos-m5.pos), radius=0.01)

dt = 0.01  # Time increment

n=0
while 1:
    rate(100)  # Increments per second

    t = n*dt   # Advance the clock.

    # Update the pendulum angles.
    q1p = Ap*cos(wp*t)
    q2p = -sqrt(2)*Ap*cos(wp*t)
    q1m = Am*cos(wm*t)
    q2m = sqrt(2)*Am*cos(wm*t)

    # Update the positions of the masses.
    m1.pos = vector(l*sin(q1p),-l*cos(q1p),0) + oa
    m2.pos = vector(l*(sin(q1p)+sin(q2p)),
                    -l*(cos(q1p)+cos(q2p)),0) + oa
    m3.pos = vector(l*sin(q1m),-l*cos(q1m),0) + ob
    m4.pos = vector(l*(sin(q1m)+sin(q2m)),
                    -l*(cos(q1m)+cos(q2m)),0) + ob
    m5.pos = vector(l*sin(q1p+q1m),-l*cos(q1p+q1m),0) + oc
    m6.pos = vector(l*(sin(q1p+q1m)+sin(q2p+q2m)),
                    -l*(cos(q1p+q1m)+cos(q2p+q2m)),0) + oc

    # Update the positions and orientations of the strings.
    string1.axis=(m1.pos-pivota.pos)
    string2.pos=m1.pos
    string2.axis=(m2.pos-m1.pos)
    string3.axis=(m3.pos-pivotb.pos)
    string4.pos=m3.pos
    string4.axis=(m4.pos-m3.pos)
    string5.axis=(m5.pos-pivotc.pos)
    string6.pos=m5.pos
    string6.axis=(m6.pos-m5.pos)

    n = n+1   # Advance the clock counter.
