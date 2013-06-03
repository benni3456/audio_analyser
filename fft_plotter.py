# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:40:50 2013

@author: be2257
"""
from pylab import *
from calc import *
from numpy import *
import scipy
import scipy.fftpack

class FFTPlotter:
    def __init__(self, PlotSpek, fs=44100):

        self.PlotSpek = PlotSpek
        self.fs = fs
        self.blocklength = 2048
        self.data = zeros(self.blocklength)
        self.recursive_weight = 0.1

    def plot(self,data):
        ''' function to plot the estimated power spectral densitiy '''

        self.data_new = dB(abs(scipy.fft(data[:self.blocklength])))
        self.data_new = self.data_new[0][0:len(self.data_new[0])/2]

        # recursive power spectral density estimation
        self.data = self.recursive_weight*self.data_new+(1-self.recursive_weight)*self.data
        
        self.PlotSpek.axes.semilogx(linspace(0,self.fs/4,len(self.data)),self.data) 
        self.PlotSpek.axes.set_xlim(0,self.fs/2)
        self.PlotSpek.axes.set_ylim(-100,50)
        self.PlotSpek.draw()