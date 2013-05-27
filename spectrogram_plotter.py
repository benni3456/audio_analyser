'''
Created on 13.05.2013

@author: Christopher
'''

from pylab import *
from calc import *
from numpy import sum


class Spectrogram_Plot():
    '''Class to Plot the spectrogram'''
    
    def __init__(self, PlotSpecgram):
        self.PlotSpecgram = PlotSpecgram
        
    def plotspecgram(self,data,fs,nfft=256):
        self.PlotSpecgram.axes.specgram(sum(data,axis=0), NFFT=nfft, Fs=fs, noverlap=0.5*nfft)
        #self.PlotSpecgram.axes.set_yscale('log')
        self.PlotSpecgram.draw()       