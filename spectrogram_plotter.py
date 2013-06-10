'''
Created on 13.05.2013

@author: Christopher
'''

#===============================================================================
# from pylab import *
# from calc import *
# from numpy import sum
#===============================================================================

from pylab import *
from calc import *
from numpy import sum
from sound_device import SAMPLING_RATE as fs

SMOOTH_DISPLAY_TIMER_PERIOD_MS = 25
DEFAULT_TIMERANGE = 2*SMOOTH_DISPLAY_TIMER_PERIOD_MS


class Spectrogram_Plot():
    '''Class to Plot the spectrogram'''
    
    def __init__(self, PlotSpecgram,audiobuffer):
        self.PlotSpecgram = PlotSpecgram
        self.audiobuffer = audiobuffer
    def plotspecgram(self,nfft=256):
        
        data = self.audiobuffer.newdata()
        nchannel,length = data.shape
        
        #=======================================================================
        # if nchannel >1:
        #     data = sum(data,axis=0)
        #=======================================================================
        
        self.PlotSpecgram.axes.specgram(sum(data,axis=0), NFFT=nfft, Fs=fs, noverlap=0.5*nfft)
        #self.PlotSpecgram.axes.set_yscale('log')
        self.PlotSpecgram.draw() 