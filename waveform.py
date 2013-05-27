# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:31:26 2013

@author: be2257
"""
class Oszi:
    def __init__(self, PlotOszi, fs):
        self.PlotOszi = PlotOszi
        
    def plot(self,data):
        ''' function to plot the waveform '''
        self.PlotOszi.axes.plot(data[0])
        self.PlotOszi.axes.set_ylim(-1,1)        
        self.PlotOszi.draw()