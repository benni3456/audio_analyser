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
        self.data = zeros(2205)  # von 1102 auf 2205 geändert !!! 

    def plot(self,data):
        ''' function to plot the level over time '''


        self.data_new = dB(abs(scipy.fft(data)))
        self.data_new = self.data_new[0][0:len(self.data_new[0])/2]
        self.data = 0.1*self.data_new+0.9*self.data
        
        #=======================================================================
        # self.PlotSpek.axes.semilogx(range(0,self.fs/4,10)[0:-1],self.data)  ' range() ist hier der falsche Befehl, lieber Linspace  verwenden
        #=======================================================================
        
        self.PlotSpek.axes.semilogx(linspace(0,self.fs/4,len(self.data)),self.data) 
        self.PlotSpek.axes.set_xlim(0,self.fs/2)
        self.PlotSpek.axes.set_ylim(-100,50)

        self.PlotSpek.draw()