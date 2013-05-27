'''
Created on 06.05.2013

@author: Christopher
'''

from pylab import *
from calc import *
import numpy as np


class ChannelPlotter:
    def __init__(self, PlotChannel):
        self.PlotChannel = PlotChannel
    
    def plot(self,data,nchannel):
        ''' function for Plotting each channel gain as a bar plot'''
        
        width = 0.5 
        channel_dB = np.zeros((nchannel),float)
        index=np.arange(nchannel)
        for i in range(nchannel):
            channel_dB[i] = dB(rms(data[i,:]))
                  
        self.PlotChannel.axes.bar(index, channel_dB+100, width, bottom=-100)
        self.PlotChannel.axes.set_ylim(-100,0)


        self.PlotChannel.axes.set_xlabel('Channels')
        
        #=======================================================================
        # xTickMarks = ['Channel'+str(i) for i in range(1,nchannel)]
        # self.PlotChannel.axes.set_xticks(index+0.01)
        # xtickNames = self.PlotChannel.axes.set_xticklabels(xTickMarks)
        # self.PlotChannel.axes.step(xtickNames,  rotation=45, fontsize=10)
        #=======================================================================
        
        self.PlotChannel.draw()