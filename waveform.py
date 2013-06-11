# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:31:26 2013

@author: be2257
"""

from pylab import *
from calc import *
from numpy import *
import scipy
import scipy.fftpack
from sound_device import SAMPLING_RATE as fs
from PyQt4 import QtGui

class Oszi:
    def __init__(self, PlotOszi, audiobuffer):
        self.PlotOszi = PlotOszi
        color = QtGui.QPalette().window().color()
        self.PlotOszi.figure.set_facecolor((color.redF(),color.greenF(),color.blueF()))
        self.audiobuffer = audiobuffer
        # number of periods to be displayed
        self.NumberOfPeriods = 4
        # undersampling factor; default=1
        self.resample = 1


    def findperiod(self,dat):
        ''' function that computes and returns possible period length within give data'''

        # extracts audio data from list; possible downsampling by factor self.resample
        data = dat[0][::self.resample]
        # finds all zero crossings in data vector
        zero_crossings = where(diff(sign(data)))

        # always returns the ascending slope of the period starting with the third period
        if data[zero_crossings[0][0]] > data[zero_crossings[0][1]]:
            # in case of odd slope
            return [zero_crossings[0][1],zero_crossings[0][1+self.NumberOfPeriods*2]]
        else:
            # in case of even slope
            return [zero_crossings[0][0],zero_crossings[0][self.NumberOfPeriods*2]]

    def plot(self):
        ''' function to plot the waveform '''
        data = self.audiobuffer.newdata()
        # calls function for indices of starting- and endpoint of self.NumberOfPeriods periods of the input vector
        zero_crossings = self.findperiod(data)
        # plots self.NumberOfPeriods periods of the input vector
        self.PlotOszi.axes.plot(data[0][zero_crossings[0]:self.resample*zero_crossings[1]])
        self.PlotOszi.axes.set_xlim(0,self.resample*zero_crossings[1]-zero_crossings[0])
        self.PlotOszi.axes.set_ylim(-1,1)
        self.PlotOszi.draw()