# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:40:50 2013

@author: be2257
"""
from pylab import *
from calc import *

class SpektroPlotter:
    def __init__(self, PlotSpektro, fs):
        self.wholestream = zeros(1)
        self.PlotSpektro = PlotSpektro
    def plot(self,data):
        ''' function to plot the level over time '''
        r_m_s = dB(rms(data))
    # recalls function gain_meter, so therefore computes the level in dB FS
        self.wholestream = concatenate([self.wholestream,[r_m_s]])
        self.PlotSpektro.axes.plot(self.wholestream[-100:])
        self.PlotSpektro.axes.set_ylim(-100,0)
        self.PlotSpektro.draw()