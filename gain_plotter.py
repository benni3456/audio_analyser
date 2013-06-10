# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:40:50 2013

@author: be2257
"""
from pylab import *
from calc import *
from sound_device import SAMPLING_RATE as fs

class GainPlotter:
    def __init__(self, PlotSpek, audiobuffer):
        '''  '''
        self.wholestream = zeros(1)
        self.PlotSpek = PlotSpek
        self.audiobuffer = audiobuffer
        
        
    def plot(self):
        ''' function to plot the level over time '''
        data = self.audiobuffer.newdata()        
        r_m_s = dB(rms(data))
        
        # recalls function gain_meter, so therefore computes the level in dB FS
        self.wholestream = concatenate([self.wholestream,[r_m_s]])
        self.PlotSpek.axes.plot(self.wholestream[-10:])
        self.PlotSpek.axes.set_ylim(-100,0)
        self.PlotSpek.draw()
        