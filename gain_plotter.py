# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:40:50 2013

@author: be2257
"""
from pylab import *
from calc import *

class GainPlotter:
    def __init__(self, PlotSpek, fs):
        self.wholestream = zeros(1)
        self.PlotSpek = PlotSpek
    def plot(self,data):
        ''' function to plot the level over time '''
        r_m_s = dB(rms(data))
    # recalls function gain_meter, so therefore computes the level in dB FS
        self.wholestream = concatenate([self.wholestream,[r_m_s]])
        self.PlotSpek.axes.plot(self.wholestream[-10:])
        self.PlotSpek.axes.set_ylim(-100,0)
        self.PlotSpek.draw()
        