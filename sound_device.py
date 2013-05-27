# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:51:13 2013

@author: Christopherus
"""

import sys
from pylab import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np

import pyaudio    
    
class SoundDeviceList(QAbstractListModel):
    def __init__(self, pa, parent=None):
        super(SoundDeviceList, self).__init__(parent)
        self.pa=pa
        
    def rowCount(self,_):                
        return self.pa.get_device_count()
        

    def data(self,index, role):
        info = self.pa.get_device_info_by_index(index.row())
        if role==Qt.DisplayRole:        
            return QVariant(QString(info["name"]))        
        else:
            return QVariant()
        
class Audioplayer(): #Audioplayer Class for using audioplayer
    def __init__(self,pa):
        self.pa=pyaudio.PyAudio()
        self.device=0
        self.fs = 48000
        self.channels = 2
        
            
    #===========================================================================
    # def noisegen(self,fs,duration):
    #     noise = randn((fs*duration),1)
    #     #noise = round(noise*2**15)/2*
    #     return noise
    #===========================================================================
    
    def setindex(self,device):
        self.device=device
    
    #===========================================================================
    # 
    # def play(self):   # Testfunction for testing the sounddevice
    #     
    #     data=self.noisegen(self.fs,self.duration)   
    #     data=array(data,dtype=float32)
    #     print(len(data))
    #     
    #     self.stream.write(data)
    #===========================================================================
            
    
    def streamopen(self):
        global stream
        stream = self.pa.open(rate=self.fs,channels=self.channels,output=True,format=pyaudio.paFloat32)
        #=======================================================================
        # print('Open Stream on %s' % self.device['name'])
        #=======================================================================
        
    def streamclose(self):
        stream.stop_stream()
        stream.close()
        print('Stream Closed')
    
    def streamread(self, stream, num_samples, num_channels):
        """
        Read samples from stream and convert them to a numpy array
    
        stream       is the stream to read from
        num_samples  is the number of samples to read
        num_channels is the number of channels to read
        """
        data = self.stream.read(num_samples)
        data = np.fromstring(data, dtype=np.float32)
        data = np.reshape(data, (len(data)/num_channels,num_channels)).T
        return data
        
