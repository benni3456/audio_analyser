# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:40:50 2013

@author: be2257
"""
from pylab import zeros
from calc import dB, rms


class Gain_Plotter:
    def __init__(self, PlotSpek, audiobuffer):
        self.wholestream = zeros(1)
        self.PlotSpek = PlotSpek
        self.audiobuffer = audiobuffer
        self.stream_data = zeros(100)

    def plot(self):
        ''' function to plot the level over time '''
        data = self.audiobuffer.newdata()

        r_m_s = dB(rms(data))

        self.stream_data[0:-1] = self.stream_data[1:]
        self.stream_data[-1] = r_m_s

        self.PlotSpek.read_array(self.stream_data)
