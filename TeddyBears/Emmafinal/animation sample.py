# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:19:57 2017

@author: fy
"""

import matplotlib.pylab as pl
import matplotlib.animation as animation


def plot(t):

    fig1=pl.figure()

    a=animation.FuncAnimation(fig1,plot,range(NT),interval=20)
    
plot(1)