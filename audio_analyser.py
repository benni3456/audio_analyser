'''
Created on 13.05.2013

@author: Christopher
'''



import sys
from pylab import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
from pyaudio import PyAudio, paFloat32
import numpy as np

import Terzpegelmesser

from scipy.signal import *
import matplotlib.pyplot as pp

#import thirds2
import waveform
import gain_plotter
import spektro_plotter
import calc
import channel_plotter
import spectrogram_plotter
import sound_device
import fft_plotter

   # Initialize PyAudio
pa = PyAudio()

    # Get some information about the default audio hardware
default_device = pa.get_default_input_device_info()
fs = int(default_device['defaultSampleRate'])
channels = 2    #default_device['maxInputChannels']

    # audio signal defined as stream
stream = None

    # just reads the data
def easy_read(stream, num_samples, num_channels):
    """
    Read samples from stream and convert them to a numpy array

    stream       is the stream to read from
    num_samples  is the number of samples to read
    num_channels is the number of channels to read
    """
    data = stream.read(num_samples)
    data = np.fromstring(data, dtype=np.float32)
    data = np.reshape(data, (len(data)/num_channels,num_channels)).T
    return data


    
def openstream():
    # open an input stream using the default audio de
    global stream
    
    stream = pa.open(rate=fs,
                     channels=channels,
                     format=paFloat32,
                     input=True)
    print('Open Stream on %s' % default_device['name'])
    
def closestream():
    stream.stop_stream()
    stream.close()
    print('Stream Closed')
    
    
    # main class combines the GUI with functions   
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui=Terzpegelmesser.Ui_MainWindow()
        self.ui.setupUi(self)        
        self.timer = QTimer(self)
        self.timer.setInterval(100) 
        
        #=======================================================================
        # self.sounddevice = sound_device.SoundDeviceList(self)
        #=======================================================================
        self.ui.DeviceList.setModel(sound_device.SoundDeviceList(pa))        
        
        self.gain_plotter = gain_plotter.GainPlotter(self.ui.PlotGainVerlauf, fs)
        self.spektro_plotter = spektro_plotter.SpektroPlotter(self.ui.PlotTerzpegel, fs)        
        self.waveform = waveform.Oszi(self.ui.PlotWellenform, fs)
        self.channelplotter = channel_plotter.ChannelPlotter(self.ui.PlotKanalpegel)
        self.specgramplot = spectrogram_plotter.Spectrogram_Plot(self.ui.PlotSpektrogramm)
        self.fft_plot = fft_plotter.FFTPlotter(self.ui.PlotFFT)
        
        
    # if the startStop button is clicked, the timer starts and the stream is filled with acoustic data
        self.ui.ButtonStartStop.clicked.connect(self.stream_run)
        self.timer.timeout.connect(self.plot)
        
    def plot(self):
        samples = easy_read(stream, int(fs/10), channels)        
  #      thirdlist = thirds2.third(samples)

        
        self.channelplotter.plot(samples,channels )
        
        self.gain_plotter.plot(samples)
        
        self.spektro_plotter.plot(samples)
        
        self.waveform.plot(samples)
        
        self.specgramplot.plotspecgram(samples, fs)
        
        self.fft_plot.plot(samples)
        
    # opens stream if there is none, else closes it  
    def stream_run(self):
        global stream
        if stream == None:
            openstream()
            self.timer.start()
        else:
            closestream()
            self.timer.stop()
            stream = None

        
if __name__ == '__main__':
    app = QApplication.instance() or QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())        