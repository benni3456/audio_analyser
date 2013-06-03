# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:51:13 2013

@author: Christopherus
Sound_device manage the sound devices of the pc. 
It is usefull to pick the right sound device and manage the audio input.
"""

from PyQt4 import QtCore
from pyaudio import PyAudio, paInt32
from numpy import floor, int32, fromstring, vstack, iinfo, float64


SAMPLING_RATE = 44100
FRAMES_PER_BUFFER = 1024 


class AudioDevice(QtCore.QObject):
    def __init__(self, logger):
        QtCore.QObject.__init__(self)
        self.logger = logger
  
        self.duo_input = False

        self.logger.push("Initializing PyAudio")
        self.pa = PyAudio()

        # look for devices
        self.input_devices = self.get_input_devices()
        self.output_devices = self.get_output_devices()

        for device in self.input_devices:
            self.logger.push("Opening the stream")
            self.stream = self.open_stream(device)
            self.device = device

            self.logger.push("Trying to read from input device %d" %device)
            if self.try_input_stream(self.stream):
                self.logger.push("Success")
                break
            else:
                self.logger.push("Fail")

        self.first_channel = 0
        nchannels = self.get_current_device_nchannels()
        if nchannels == 1:
            self.second_channel = 0
        else:
            self.second_channel = 1

        # counter for the number of input buffer overflows
        self.xruns = 0
        
            # method
    def get_readable_devices_list(self):
        devices_list = []
        
        default_device_index = self.get_default_input_device()
        
        for device in self.input_devices:
            dev_info = self.pa.get_device_info_by_index(device)
            api = self.pa.get_host_api_info_by_index(dev_info['hostApi'])['name']

            if device is default_device_index:
                extra_info = ' (system default)'
            else:
                extra_info = ''
            
            nchannels = self.pa.get_device_info_by_index(device)['maxInputChannels']
   
            desc = "%s (%d channels) (%s) %s" %(dev_info['name'], nchannels, api, extra_info)
            
            devices_list += [desc]            

        return devices_list

    # method
    def get_readable_output_devices_list(self):
        devices_list = []
        
        default_device_index = self.get_default_output_device()
        
        for device in self.output_devices:
            dev_info = self.pa.get_device_info_by_index(device)
            api = self.pa.get_host_api_info_by_index(dev_info['hostApi'])['name']

            if device is default_device_index:
                extra_info = ' (system default)'
            else:
                extra_info = ''
            
            nchannels = self.pa.get_device_info_by_index(device)['maxOutputChannels']
   
            desc = "%s (%d channels) (%s) %s" %(dev_info['name'], nchannels, api, extra_info)
            
            devices_list += [desc]            

        return devices_list

    # method
    def get_default_input_device(self):
        return self.pa.get_default_input_device_info()['index']

    # method
    def get_default_output_device(self):
        return self.pa.get_default_output_device_info()['index']

    # method
    def get_device_count(self):
        # FIXME only input devices should be chosen, not all of them !
        return self.pa.get_device_count()

    # method
    # returns a list of input devices index, starting with the system default
    def get_input_devices(self):
        device_count = self.get_device_count()
        default_input_device = self.get_default_input_device()
        
        device_range = range(0, device_count)
        # start by the default input device
        device_range.remove(default_input_device)
        device_range = [default_input_device] + device_range

        # select only the input devices by looking at the number of input channels
        input_devices = []
        for device in device_range:
            n_input_channels = self.pa.get_device_info_by_index(device)['maxInputChannels']
            if n_input_channels > 0:
                input_devices += [device]
        
        return input_devices

    # method
    # returns a list of output devices index, starting with the system default
    def get_output_devices(self):
        device_count = self.get_device_count()
        default_output_device = self.get_default_output_device()
        
        device_range = range(0, device_count)
        # start by the default input device
        device_range.remove(default_output_device)
        device_range = [default_output_device] + device_range

        # select only the output devices by looking at the number of output channels
        output_devices = []
        for device in device_range:
            n_output_channels = self.pa.get_device_info_by_index(device)['maxOutputChannels']
            if n_output_channels > 0:
                output_devices += [device]
        
        return output_devices

    # method
    def select_input_device(self, device):
        # save current stream in case we need to restore it
        previous_stream = self.stream
        previous_device = self.device

        self.stream = self.open_stream(device)
        self.device = device

        self.logger.push("Trying to read from input device #%d" % (device))
        if self.try_input_stream(self.stream):
            self.logger.push("Success")
            previous_stream.close()
            success = True   
   
            self.first_channel = 0
            nchannels = self.get_current_device_nchannels()
            if nchannels == 1:                
                self.second_channel = 0
            else:
                self.second_channel = 1
        else:
            self.logger.push("Fail")
            self.stream.close()
            self.stream = previous_stream
            self.device = previous_device
            success = False

        return success, self.device

    # method
    def select_first_channel(self, index):
        self.first_channel = index
        success = True
        return success, self.first_channel

    # method
    def select_second_channel(self, index):
        self.second_channel = index
        success = True
        return success, self.second_channel

    # method
    def open_stream(self, device):
        ''' by default we open the device stream with all the channels
        # (interleaved in the data buffer)'''
        maxInputChannels = self.pa.get_device_info_by_index(device)['maxInputChannels']
        stream = self.pa.open(format=paInt32, channels=maxInputChannels, rate=SAMPLING_RATE, input=True,
                frames_per_buffer=FRAMES_PER_BUFFER, input_device_index=device)
        return stream

    # method
    # return the index of the current input device in the input devices list
    # (not the same as the PortAudio index, since the latter is the index
    # in the list of *all* devices, not only input ones)
    def get_readable_current_device(self):
        i = 0
        for device in self.input_devices:
            if device == self.device:
                break
            else:
                i += 1
        return i

    # method
    def get_readable_current_channels(self):            
        dev_info = self.pa.get_device_info_by_index(self.device)  
        nchannels = dev_info['maxInputChannels']

        if nchannels == 2:
            channels = ['L', 'R']
        else:
            channels = []
            for channel in range(0, dev_info['maxInputChannels']):
                channels += ["%d" %channel]            
            
        return channels

    # method
    def get_current_first_channel(self):
        return self.first_channel

    # method
    def get_current_second_channel(self):
        return self.second_channel

    # method    
    def get_current_device_nchannels(self):
        return self.pa.get_device_info_by_index(self.device)['maxInputChannels']

    # method
    # return True on success
    def try_input_stream(self, stream):
        n_try = 0
        while stream.get_read_available() < FRAMES_PER_BUFFER and n_try < 1000000:
            n_try +=1

        if n_try == 1000000:
            return False
        else:
            lat_ms = 1000*stream.get_input_latency()
            self.logger.push("Device claims %d ms latency" %(lat_ms))
            return True

      # try to update the audio buffer
    # return the number of chunks retrieved, and the time elapsed
    def update(self, ringbuffer):
        t = QtCore.QTime()
        t.start()
        
        channel = self.get_current_first_channel()
        nchannels = self.get_current_device_nchannels()
        if self.duo_input:
            channel_2 = self.get_current_second_channel()
        
        chunks = 0
        
        # ask for how much data is available
        available = self.stream.get_read_available()

        # read what is available
        # we read by multiples of FRAMES_PER_BUFFER, otherwise degfaults !

        #print available, int(floor(available/FRAMES_PER_BUFFER))
        #FIXME no less than 2048 samples at each stream read ??

        available = int(floor(available/FRAMES_PER_BUFFER))
        for j in range(0, available):
            try:
                rawdata = self.stream.read(FRAMES_PER_BUFFER)
            except IOError as inst:
                # FIXME specialize this exception handling code
                # to treat overflow errors particularly
                self.xruns += 1
                print "Caught an IOError on stream read.", inst
                break
            
            intdata_all_channels = fromstring(rawdata, int32)

            int32info = iinfo(int32)
            norm_coeff = max(abs(int32info.min), int32info.max)
            floatdata_all_channels = intdata_all_channels.astype(float64)/float(norm_coeff)


            floatdata1 = floatdata_all_channels[channel::nchannels]

            if self.duo_input:                                        
                floatdata2 = floatdata_all_channels[channel_2::nchannels]
                floatdata = vstack((floatdata1, floatdata2))
            else:  
                floatdata = floatdata1
                floatdata.shape = (1, FRAMES_PER_BUFFER)
            
            # update the circular buffer
            ringbuffer.push(floatdata)
            chunks += 1
        
        return (chunks, t.elapsed(), chunks*FRAMES_PER_BUFFER)
  
    def set_single_input(self):
        self.duo_input = False

    def set_duo_input(self):
        self.duo_input = True

    # returns the stream time in seconds
    def get_stream_time(self):
        return self.stream.get_time()


#===============================================================================
# import sys
# from pylab import *
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# import numpy as np
# 
# from pyaudio import PyAudio, paFloat32  
#     
# class AudioDevice(QAbstractListModel):
#     def __init__(self, pa, parent=None):
#         super(AudioDevice, self).__init__(parent)
#         self.pa=pa
#         
#     def rowCount(self,_):                
#         return self.pa.get_device_count()
#         
# 
#     def data(self,index, role):
#         info = self.pa.get_device_info_by_index(index.row())
#         if role==Qt.DisplayRole:        
#             return QVariant(QString(info["name"]))        
#         else:
#             return QVariant()
#         
# class Audioplayer(): #Audioplayer Class for using audioplayer
#     def __init__(self,pa):
#         self.pa=PyAudio()
#         self.device=0
#         self.fs = 48000
#         self.channels = 2
#         
#             
#     #===========================================================================
#     # def noisegen(self,fs,duration):
#     #     noise = randn((fs*duration),1)
#     #     #noise = round(noise*2**15)/2*
#     #     return noise
#     #===========================================================================
#     
#     def setindex(self,device):
#         self.device=device
#     
#     #===========================================================================
#     # 
#     # def play(self):   # Testfunction for testing the sounddevice
#     #     
#     #     data=self.noisegen(self.fs,self.duration)   
#     #     data=array(data,dtype=float32)
#     #     print(len(data))
#     #     
#     #     self.stream.write(data)
#     #===========================================================================
#             
#     
#     def streamopen(self):
#         global stream
#         stream = self.pa.open(rate=self.fs,channels=self.channels,output=True,format=paFloat32)
#         #=======================================================================
#         # print('Open Stream on %s' % self.device['name'])
#         #=======================================================================
#         
#     def streamclose(self):
#         stream.stop_stream()
#         stream.close()
#         print('Stream Closed')
#     
#     def streamread(self, stream, num_samples, num_channels):
#         """
#         Read samples from stream and convert them to a numpy array
#     
#         stream       is the stream to read from
#         num_samples  is the number of samples to read
#         num_channels is the number of channels to read
#         """
#         data = self.stream.read(num_samples)
#         data = np.fromstring(data, dtype=np.float32)
#         data = np.reshape(data, (len(data)/num_channels,num_channels)).T
#         return data
#         
#===============================================================================
