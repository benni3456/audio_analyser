'''
Created on 13.05.2013

@author: Christopher
'''

from pylab import *
from calc import *
from numpy import sum
from sound_device import SAMPLING_RATE as fs
from PyQt4 import QtCore, QtGui


SMOOTH_DISPLAY_TIMER_PERIOD_MS = 25
DEFAULT_TIMERANGE = 2*SMOOTH_DISPLAY_TIMER_PERIOD_MS

class Spectrogram_Plot():
    '''Class to Plot the spectrogram'''
    
    def __init__(self, PlotSpecgram,audiobuffer):
        
        
        self.PlotSpecgram = PlotSpecgram
        
        self.audiobuffer = audiobuffer
        
        
        #=======================================================================
        # if logger is None:
        #     self.logger = parent.parent.logger
        # else:
        #     self.logger = logger
        #=======================================================================
        
        self.timerange = DEFAULT_TIMERANGE
        
        #=======================================================================
        # pxx,freqs,bins = mlab.specgram(rand(10,float32), NFFT=nfft, Fs=44100, noverlap=0.5*nfft)
        # self.PlotSpecgram.axes.set_yscale('symlog', linthreshy=0.01)
        # self.PlotSpecgram.axes.pcolormesh(bins, freqs, 10 * np.log10(pxx))
        # self.PlotSpecgram.axes.axis('tight')
        #=======================================================================

    #===========================================================================
    # def set_buffer(self, buffer):
    #     self.audiobuffer = buffer
    #===========================================================================
        
    def update(self,nfft=256):
        # get the fresh data
        
        
        data = self.audiobuffer.newdata()
        
        print("data = "+str(data))
        print("size = "+str(data.shape))
        #=======================================================================
        # pxx, freqs, bins = mlab.specgram(sum(data,axis=0), NFFT=nfft, Fs=fs, noverlap=0.5*nfft)
        # #self.im.set_data(self.im,pxx)
        # 
        # self.PlotSpecgram.axes.pcolormesh(bins, freqs, 10 * np.log10(pxx))
        # self.PlotSpecgram.axes.axis('tight')
        # #self.PlotSpecgram.axes.set_yscale('log')
        # 
        # self.PlotSpecgram.show()
        # matplotlib.pyplot.pause(0.001)       
        #=======================================================================
        
        #self.PlotSpecgram.axes.matplotlib.pyplot.specgram(data, NFFT=nfft, Fs=fs, noverlap=0.5*nfft)
        self.PlotSpektrogram.axes.specgram(data, NFFT=nfft, Fs=fs, noverlap=0.5*nfft)
        #self.PlotSpecgram.axes.set_yscale('log')
        self.PlotSpektrogram.draw()
