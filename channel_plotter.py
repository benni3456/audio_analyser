'''
Created on 06.05.2013

@author: Christopher
'''

#from pylab import *
from calc import rms, dB
import numpy as np
#from plot_channellevel import Channel_Bar


class ChannelPlotter:
    def __init__(self, PlotChannel, audiobuffer):
        self.PlotChannel = PlotChannel
        self.audiobuffer = audiobuffer

    def plot(self):
        ''' function for Plotting each channel gain as a bar plot'''

        data = self.audiobuffer.newdata()
        nchannel, _ = data.shape

        channel_dB = np.zeros((nchannel), float)
        #index = np.arange(nchannel)
        for i in range(nchannel):
            channel_dB[i] = dB(rms(data[i, :]))

        nchannel = np.arange(nchannel)

        self.PlotChannel.readArray(channel_dB, nchannel)
