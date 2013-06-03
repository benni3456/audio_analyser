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
    def __init__(self, PlotSpek, audiobuffer, fs=48000):

        self.PlotSpek = PlotSpek
        self.audiobuffer = audiobuffer
        self.fs = fs
        self.blocklength = 8*1024
        self.data = zeros(self.blocklength/2)
        self.recursive_weight = 0.1

    def nextpow2(self,n):
        m_f = np.log2(n)
        m_i = np.floor(m_f)
        return int(m_i)

    def plot(self):
        ''' function to plot the estimated power spectral densitiy '''
        data = self.audiobuffer.newdata()

        # limitation of the blocklength to the next lower 2^n in case of drainage of buffer
        if self.blocklength > len(data[0]):
            self.blocklength = 2**(self.nextpow2(len(data[0])))
            self.data = zeros(self.blocklength/2)

        data = data[0][:self.blocklength]

        self.data_new = dB(abs(scipy.fft(data)))
        self.data_new = self.data_new[:self.blocklength/2]

        # recursive power spectral density estimation
        self.data = self.recursive_weight*self.data_new+(1-self.recursive_weight)*self.data
        
        self.PlotSpek.axes.semilogx(linspace(0,self.fs/4,len(self.data)),self.data) 
        self.PlotSpek.axes.set_xlim(0,self.fs/2)
        self.PlotSpek.axes.set_ylim(-100,50)
        self.PlotSpek.draw()