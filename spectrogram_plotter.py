'''
Created on 13.05.2013

@author: Christopher
'''

import numpy as np
from pylab import specgram
from numpy import sum
from sound_device import SAMPLING_RATE as fs
from PyQt4 import QtGui

SMOOTH_DISPLAY_TIMER_PERIOD_MS = 25
DEFAULT_TIMERANGE = 2 * SMOOTH_DISPLAY_TIMER_PERIOD_MS


class Spectrogram_Plot():
    '''Class to Plot the spectrogram'''

    def __init__(self, PlotSpecgram, audiobuffer):
        self.PlotSpecgram = PlotSpecgram
        self.audiobuffer = audiobuffer
        color = QtGui.QPalette().base().color()
        self.PlotSpecgram.figure.set_facecolor((color.redF(), color.greenF(),
                                                 color.blueF()))
        self.bufferlen = 300
        self.specdata = np.zeros((129, self.bufferlen))
        numBins, numSpectra = self.specdata.shape
        self.x = np.arange(0, numSpectra)
        self.y = np.linspace(0, fs / 2, numBins)

    def plotspecgram(self, nfft=256):

        data = self.audiobuffer.newdata()
        Pxx, _, _, _ = specgram(sum(data, axis=0),
                NFFT=nfft, Fs=fs, noverlap=0.5 * nfft)
        _, numSpectra = Pxx.shape

        Pxx = np.log10(Pxx) * 10

        self.specdata[:, 0:-numSpectra] = self.specdata[:, numSpectra:]
        self.specdata[:, -numSpectra:] = Pxx

        self.PlotSpecgram.axes.pcolormesh(self.x, self.y, self.specdata,
                                          vmin=-120, vmax=-0)
        self.PlotSpecgram.axes.axis('tight')
        self.PlotSpecgram.draw()
