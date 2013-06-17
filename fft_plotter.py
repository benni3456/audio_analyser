# -*- coding: utf-8 -*-


from calc import dB
import numpy as np
from sound_device import SAMPLING_RATE as fs
from PyQt4 import QtGui
import scipy


class FFTPlotter:
    def __init__(self, PlotSpek, audiobuffer, blocklength, plotflag=1):
        ''' function to initialize an objekt of the class FFTPlotter '''
        self.PlotSpek = PlotSpek
        color = QtGui.QPalette().base().color()
        self.PlotSpek.figure.set_facecolor((color.redF(), color.greenF(),
                                            color.blueF()))
        self.audiobuffer = audiobuffer
        self.fs = fs
        self.blocklength = blocklength
        self.blocklength_old = blocklength
        self.data = np.zeros(self.blocklength / 2)
        self.recursive_weight = 0.1
        self.plotflag = plotflag
        self.must_plot = True


    def nextpow2(self, n):
        ''' function to compute the next lower power of 2 of given input n '''
        m_f = np.log2(n)
        m_i = np.floor(m_f)
        return int(m_i)

    def plot(self, blocklength, plotflag=1):
        ''' function to plot the estimated power spectral densitiy '''

        # blocklength may be changed by user
        self.plotflag = plotflag
        self.blocklength = blocklength
        data = self.audiobuffer.newdata()

        # limitation of the blocklength to the next lower 2^n in case of
        # drainage of buffer
        if self.blocklength > len(data[0]):
            self.blocklength = 2 ** (self.nextpow2(len(data[0])))
            self.data = np.zeros(self.blocklength / 2)

        data = data[0][:self.blocklength]

        self.data_new = dB(abs(scipy.fft(data)))
        self.data_new = self.data_new[:self.blocklength / 2]

        if self.blocklength != self.blocklength_old:
            self.data = np.zeros(self.blocklength / 2)

        # recursive power spectral density estimation
        self.data = (self.recursive_weight * self.data_new
                    + (1 - self.recursive_weight) * self.data)
        self.blocklength_old = self.blocklength

        if self.must_plot:

            # plotflag 0 sets the frequency axis to linear stepping
            if self.plotflag == 0:
                self.lines, = self.PlotSpek.axes.plot(np.linspace(0,
                                                     self.fs / 2,
                                                     len(self.data)),
                                                     self.data)

                self.PlotSpek.axes.set_xlim(0, self.fs / 2)
            # plotflag 1 sets the frequency axis to logarithmic stepping
            else:
                self.lines, = self.PlotSpek.axes.semilogx(np.linspace(0,
                                    self.fs / 4, len(self.data)), self.data)
                self.PlotSpek.axes.set_xlim(0, self.fs / 2)

            self.PlotSpek.axes.set_ylim(-100, 50)
            self.PlotSpek.axes.grid(True, which='both')
            self.must_plot = False
        else:
            self.lines.set_ydata(self.data)

        self.PlotSpek.draw()
