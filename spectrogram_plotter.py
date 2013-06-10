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
        
        Pxx, freqs, bins, im = specgram(sum(data,axis=0), NFFT=nfft, Fs=fs, noverlap=0.5*nfft)
        numBins, numSpectra = Pxx.shape
        
        x = np.arange(0, numSpectra)
        y = np.arange(0, numBins)
        z = Pxx
        #=======================================================================
        # print("numSpectra = "+str(x))
        # print("numBins = "+str(y))
        # print("Pxx = "+str(z))
        # print(Pxx.shape)
        #=======================================================================

        self.PlotSpecgram.axes.pcolormesh(x,y,z)
        #self.PlotSpecgram.axes.set_yscale('symlog')
        self.PlotSpecgram.axes.axis('tight')

        
        
        
        #=======================================================================
        # im.set_data(x, y, z)
        # self.PlotSpecgram.axes.images.append(im) 
        # self.PlotSpecgram.axes.set_xlim(0,numSpectra)
        # self.PlotSpecgram.axes.set_ylim(0,numBins)
        # self.PlotSpecgram.axes.set_yscale('symlog')
        #=======================================================================
        #self.PlotSpecgram.axes.set_yscale('log')
        
        self.PlotSpecgram.draw() 