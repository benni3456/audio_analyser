'''
Created on 13.05.2013

@author: Christopher
'''

from pylab import specgram
import numpy as np
from numpy import sum
from sound_device import SAMPLING_RATE as fs

SMOOTH_DISPLAY_TIMER_PERIOD_MS = 25
DEFAULT_TIMERANGE = 2 * SMOOTH_DISPLAY_TIMER_PERIOD_MS


class Spectrogram_Plot():
    '''Class to Plot the spectrogram'''

    def __init__(self, PlotSpecgram, audiobuffer):
        self.PlotSpecgram = PlotSpecgram
        self.audiobuffer = audiobuffer

    def plotspecgram(self, nfft = 256):

        data = self.audiobuffer.newdata()
        Pxx, freqs, bins, im = specgram(sum(data, axis = 0),
                NFFT = nfft, Fs = fs, noverlap = 0.5 * nfft)
        numBins, numSpectra = Pxx.shape

        x = np.arange(0, numSpectra)
        y = np.arange(0, numBins)
        z = Pxx

        self.PlotSpecgram.axes.pcolormesh(x, y, z)
        self.PlotSpecgram.axes.axis('tight')
        self.PlotSpecgram.draw()
