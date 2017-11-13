#!/usr/bin/python2.2

from visual import *
import math

class planeWave:
    def __init__(self,
                 fr          = None,
                 r           = vector(0,0,0),
                 C           = 10,
                 omega       = pi,
                 k           = pi/4,
                 phi         = 0,
                 graphLength = None,
                 nGraph      = None,
                 graphRadius = None,
                 graphColor  = color.white,
                 pointRadius = None,
                 pointColor  = color.blue,
                 dt          = 0.01,
                 f           = 30):
        self.fr           = fr  
        self.r            = vector(r)
        self.C            = C
        self.omega        = omega
        self.k            = k
        self.phi          = phi
        self.graphLength = graphLength
        if self.graphLength == None:
            self.graphLength = 3.0*self.C
        self.nGraph = nGraph
        if self.nGraph == None:
            self.nGraph = 100.0
        self.graphRadius  = graphRadius
        if self.graphRadius == None:
            self.graphRadius  = self.C/50.0
        self.graphColor   = graphColor
        self.pointRadius  = pointRadius
        if self.pointRadius == None:
            self.pointRadius  = 4.0*self.graphRadius
        self.pointColor   = pointColor
        self.dt           = dt
        self.f            = f
        self.circleOrigin = self.r + vector(0, -2*self.C, 0)
        self.pointRo      = self.circleOrigin + vector(self.C, 0, 0)
        self.graphOrigin  = self.r

        self.xAxis    = cylinder(frame  = self.fr,
                                 pos    = self.graphOrigin,
                                 radius = self.graphRadius,
                                 axis   = vector(0,1,0),
                                 length = self.graphLength,
                                 color  = color.white)

        self.circle    = ring(frame       = self.fr,
                              pos         = self.circleOrigin,
                              axis        = vector(0,0,1),
                              radius      = self.C + self.graphRadius/2.0,
                              thickness   = self.graphRadius,
                              color       = self.pointColor)

        self.point     = sphere(frame  = self.fr,
                                pos         = self.pointRo,
                                radius      = self.pointRadius,
                                color       = self.pointColor)

        self.magnitude = cylinder(frame  = self.fr,
                                  pos    = self.circleOrigin,
                                  axis   = self.point.pos-self.circleOrigin,
                                  radius = self.graphRadius,
                                  color  = self.pointColor)

        self.realPart  = cylinder(frame  = self.fr,
                                  pos    = self.circleOrigin,
                                  axis   = vector(self.point.pos.x, 0, 0),
                                  radius = self.graphRadius,
                                  color  = self.graphColor)

        self.y         = arange(0,
                                self.graphLength \
                                + self.graphLength/float(self.nGraph),
                                self.graphLength/float(self.nGraph))

        self.graph     = curve(frame  = self.fr,
                               x      = self.graphOrigin.x + \
                                        self.C*cos(self.k*self.y + self.phi),
                               y      = self.graphOrigin.y + self.y,
                               radius = self.graphRadius,
                               color  = self.graphColor)
        self.n = 0
        return
        
    def step(self, dt = None):
        if dt != None:
            self.dt = dt
        self.n = self.n + 1
        t = self.n*self.dt
        self.point.pos     = self.circleOrigin \
                             + vector(self.C*cos(-self.omega*t+self.phi),
                                      self.C*sin(-self.omega*t+self.phi), 0)
        self.magnitude.axis = self.point.pos - self.circleOrigin
        self.realPart.axis  = vector((self.point.pos.x \
                                      - self.circleOrigin.x),
                                      0, 0)
                              
        self.graph.x = self.graphOrigin.x \
                       + self.C*cos(self.k*self.y-self.omega*t+self.phi)
        rate(self.f)
        return

class superposition:
    def __init__(self,
                 fr          = None,
                 graphRadius = None,
                 graphColor  = color.white,
                 pointRadius = None,
                 pointColor  = color.blue,
                 dt          = None,
                 f           = 30):
        self.fr           = fr
        self.graphRadius  = graphRadius
        self.graphColor   = graphColor
        self.pointRadius  = pointRadius
        self.pointColor   = pointColor
        self.dt           = dt
        self.f            = f
        self.waves = []
        return
    
    def append(self,
               wave = None):
        if self.graphRadius == None and wave.graphRadius > self.graphRadius:
            self.graphRadius = wave.graphRadius
        if self.pointRadius == None and wave.pointRadius > self.pointRadius:
            self.pointRadius = wave.pointRadius
        self.waves.append(wave)
        if len(self.waves) == 1:
            self.x = self.waves[0].graph.x*0.0
            self.y = self.waves[0].y + self.waves[0].graphOrigin.y
            self.graph = curve(frame  = self.fr,
                               x      = self.x,
                               y      = self.y,
                               radius = self.graphRadius,
                               color  = self.graphColor)
        if self.dt == None:
            for wave in self.waves:
                if self.dt == None:
                    self.dt = wave.dt
        if self.dt == None:
            self.dt = 0.01
        return

    def step(self, dt=None):
        if dt != None:
            self.dt = dt
        self.waves[0].step(dt = self.dt)
        x = self.waves[0].graph.x
        for wave in self.waves[1:]:
            wave.step(dt = self.dt)
            x = x + wave.graph.x - wave.graphOrigin.x
        self.graph.x = x
        return
        
if __name__ == '__main__':
    H    = 600         # Scene height [pixels]
    W    = 250         # Scene width  [pixels]
    scene.title = 'Plane Wave'
    scene.height = H
    scene.width = W
    scene.autoscale = 0
    scene.range = vector(35, 35, 35)

    w = planeWave()
    while 1:
        w.step()
