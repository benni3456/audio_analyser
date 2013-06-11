'''
Created on 13.05.2013

@author: Christopher
'''



import sys
from pylab import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np

import time
from audio_buffer import AudioBuffer # audio ring buffer class
from sound_device import AudioDevice# audio device class
from log_class import Logger 
#from sound_settings import Settings_Dialog


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



SMOOTH_DISPLAY_TIMER_PERIOD_MS = 25
    
    
# main class combines the GUI with functions   
class MainWindow(QMainWindow):
    def __init__(self,logger):
        self.logger = logger
               
        super(MainWindow,self).__init__()
        self.ui=Terzpegelmesser.Ui_MainWindow()
        self.ui.setupUi(self)        
        
        #self.settings_dialog = Settings_Dialog(self)
        
        self.chunk_number = 0
        self.buffer_timer_time = 0.
        self.cpu_percent = 0.
        
        # Initialize the audio data ring buffer
        self.audiobuffer = AudioBuffer(self.logger)

        # Initialize the audio device
        self.audio_device = AudioDevice(self.logger)

        # Initialize the blocklength
        self.blocklength = 2048

        # Initialize the frequency weighting flag
        self.weight = 0

        # Initialize the number of samples shown in oscilloscope
        self.window = 128

        # Initialize the flag for lin (0) and log (1) fft plotting
        self.plotflag = 1


        devices = self.audio_device.get_readable_devices_list()
        for device in devices:
            self.ui.DeviceList.addItem(device)

        channels = self.audio_device.get_readable_current_channels()
        #=======================================================================
        # for channel in channels:
        #     self.settings_dialog.comboBox_firstChannel.addItem(channel)
        #     self.settings_dialog.comboBox_secondChannel.addItem(channel)
        #=======================================================================

        current_device = self.audio_device.get_readable_current_device()
        self.ui.DeviceList.setCurrentIndex(current_device)
                   
        #=======================================================================
        # self.timer = QTimer(self)
        # self.timer.setInterval(100) 
        #=======================================================================
        
        self.display_timer = QTimer()
        self.display_timer.setInterval(SMOOTH_DISPLAY_TIMER_PERIOD_MS) # constant timing
        
        self.connect(self.display_timer, SIGNAL('timeout()'), self.update_buffer)
        #self.connect(self.display_timer, SIGNAL('timeout()'), self.statistics)

        
        self.connect(self.ui.ButtonStartStop, SIGNAL('triggered()'), self.stream_run)
        self.connect(self.ui.DeviceList, SIGNAL('currentIndexChanged(int)'), self.input_device_changed)
        #self.connect(self.settings_dialog.comboBox_firstChannel, SIGNAL('currentIndexChanged(int)'), self.first_channel_changed)
        #self.connect(self.settings_dialog.comboBox_secondChannel, SIGNAL('currentIndexChanged(int)'), self.second_channel_changed)

        self.connect(self.ui.BoxFFT, SIGNAL('currentIndexChanged(int)'), self.update_blocklength)
        self.connect(self.ui.BoxBew, SIGNAL('currentIndexChanged(int)'), self.update_weight)

        self.connect(self.ui.RadioLin, SIGNAL("clicked()"), self.update_plotflag_lin)
        self.connect(self.ui.RadioLog, SIGNAL("clicked()"), self.update_plotflag_log)

        #=======================================================================
        # self.ui.DeviceList.setModel(sound_device.AudioDevice())        
        #=======================================================================
        
        
        # Plot Connection t
        
        
        self.gain_plotter = gain_plotter.GainPlotter(self.ui.PlotGainVerlauf, self.audiobuffer)
        self.spektro_plotter = spektro_plotter.SpektroPlotter(self.ui.PlotTerzpegel,self.audiobuffer)        
        self.waveform = waveform.Oszi(self.ui.PlotWellenform,self.audiobuffer)
        self.channelplotter = channel_plotter.ChannelPlotter(self.ui.PlotKanalpegel,self.audiobuffer)
        
        #self.specgramplot = spectrogram_plotter.Spectrogram_Plot(self.ui.PlotSpektrogramm)
        self.specgramplot = spectrogram_plotter.Spectrogram_Plot(self.ui.PlotSpektrogramm, self.audiobuffer)
        
        self.fft_plot = fft_plotter.FFTPlotter(self.ui.PlotFFT,self.audiobuffer,self.blocklength,self.plotflag)
        
        
    # if the startStop button is clicked, the timer starts and the stream is filled with acoustic data
        self.ui.ButtonStartStop.clicked.connect(self.stream_run)
        self.ui.ButtonStartStop.state = 0
        self.display_timer.timeout.connect(self.update_plot)
        
    def update_plot(self):

        #=======================================================================
        self.channelplotter.plot()
        #  
        #self.gain_plotter.plot()
        #  
        self.spektro_plotter.plot(self.weight)
        #  
        self.waveform.plot()
        #  
        #=======================================================================
        #self.specgramplot.plotspecgram(self,self.logger)
        #self.specgramplot.plotspecgram()
         
        #=======================================================================
        self.fft_plot.plot(self.blocklength,self.plotflag)
        #=======================================================================
        time.sleep(0.01)
    # opens stream if there is none, else closes it  
    def stream_run(self):
        
        if (self.ui.ButtonStartStop.state==0):
            #openstream()
            self.logger.push("Timer start")
            self.display_timer.start()
            self.ui.ButtonStartStop.setText("Stop")
            #self.timer.start()
            self.display_timer.start()
            #print(logger.log)
            self.ui.ButtonStartStop.state = 1
        else:
            #closestream()
            self.logger.push("Timer stop")
            self.display_timer.stop()
            self.ui.ButtonStartStop.setText("Start")
            #self.timer.stop()
            self.display_timer.stop()
            self.ui.ButtonStartStop.state = 0
            print(logger.log)
            
    def update_buffer(self):
        chunks, t, newpoints = self.audio_device.update(self.audiobuffer.ringbuffer)
        self.audiobuffer.set_newdata(newpoints)
        self.chunk_number += chunks
        self.buffer_timer_time = (95.*self.buffer_timer_time + 5.*t)/100.


    def update_blocklength(self,newblocklength):
        self.blocklength = 32*(2**newblocklength)
        print 'Blocksize changed to', self.blocklength

    def update_weight(self,weight):
        self.weight = weight
        if self.weight == 0:
            print 'Using Z Curve (unweighted)'
        elif self.weight == 1:
            print 'Using A Curve'
        elif self.weight == 2:
            print 'Using C Curve'

    def update_plotflag_lin(self):
        self.plotflag = 0
        print 'Linear frequency axis selected'

    def update_plotflag_log(self):
        self.plotflag = 1
        print 'Logarithmic frequency axis selected'


    def input_device_changed(self, index):
        #self.ui.actionStart.setChecked(False)
        
        success, index = self.audio_device.select_input_device(index)
        
        self.ui.DeviceList.setCurrentIndex(index)
        
        if not success:
            # Note: the error message is a child of the settings dialog, so that
            # that dialog remains on top when the error message is closed
            error_message = QErrorMessage(self.settings_dialog)
            error_message.setWindowTitle("Input device error")
            error_message.showMessage("Impossible to use the selected input device, reverting to the previous one")
        
        # reset the channels
  #=============================================================================
  #       first_channel = self.audio_device.get_current_first_channel()
  #       self.settings_dialog.comboBox_firstChannel.setCurrentIndex(first_channel)
  #       second_channel = self.audio_device.get_current_second_channel()
  #       self.settings_dialog.comboBox_secondChannel.setCurrentIndex(second_channel)  
  # 
  #       self.ui.actionStart.setChecked(True)
  #=============================================================================

    def statistics(self):
        if not self.about_dialog.LabelStats.isVisible():
            return
             
        label = "Chunk #%d\n"\
        "Audio buffer retrieval: %.02f ms\n"\
        "Global CPU usage: %d %%\n"\
        "Number of overflowed inputs (XRUNs): %d"\
        % (self.chunk_number, self.buffer_timer_time, self.cpu_percent, self.audio_device.xruns)
        
        self.about_dialog.LabelStats.setText(label)
      
      
if __name__ == '__main__':
    app = QApplication.instance() or QApplication(sys.argv)
    logger = Logger()
    frame = MainWindow(logger)
    frame.show()
    sys.exit(app.exec_())        
