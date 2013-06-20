"""
Created on Mon Apr 29 15:00:40 2013

@author: ol2172
"""

#!/usr/bin/python

# gain_plot.py
from __future__ import division
from PyQt4 import QtGui, QtCore
from pylab import arange
import numpy as np


class GainPlotter(QtGui.QWidget):
    """ Plots the gain (input array) of audio signal in dB as
    a function of time

        The values of the last 30 seconds are shown.

    """

    def __init__(self, parent=None, Ymax_min=80):
        """ Function to generate layout for the plot """
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 200, 1000, 500)
        self.setWindowTitle('graphic')
        self.y_range = Ymax_min
        self.y_ticks = range(-80, 20, 20)
        # gain-values in array
        self.dBValue = np.zeros(100)
        # gain-values in array
        self.timeValue = range(0, 100)
        # time-array from 0s to -30s (to plot data of the last 30s)
        self.timestep = range(-30, 1)
        # calculate temporal distance between two sequent values
        self.temporaldist = 1 / (len(self.dBValue) / 30)

    def read_array(self, dBValue, timeValue=arange(0, 100, 1)):
        """ Function to read input data arrays """
        #assert (len(dBValue) == len(time_value))
        self.dBValue = dBValue
        self.timeValue = timeValue

    def draw_text(self, painter):
        """ Function to title and to label the axis
        of abscissae and the ordinate """
        # title the axes (ordinate: gain-axis in dB, absissae: time-axis in s)
        painter.drawText(QtCore.QRectF(self.width() - 200, 20, 20, 20),
                            QtCore.Qt.AlignCenter, ' t/s ')
        painter.drawText(QtCore.QRectF(-30, -self.height() + 160, 40, 20),
                            QtCore.Qt.AlignCenter, ' gain/dB ')
        # label axis of abscissae
        startpoint = 1
        stepsize = (self.width() - 200) / (len(self.timestep))
        for i in range(0, len(self.timestep), 1):
            painter.drawText(QtCore.QRectF(startpoint, 0, 2 * stepsize, 20),
                             QtCore.Qt.AlignCenter, str(self.timestep[i]))
            startpoint = startpoint + (
                                self.width() - 200) / (len(self.timestep))
        # label ordinate
        y_axis_lines = 5
        y_axis = -10
        for i in range(0, y_axis_lines):
            painter.drawText(QtCore.QRectF(-30, y_axis, 20, 20),
                             QtCore.Qt.AlignCenter, str(self.y_ticks[i]))
            y_axis = y_axis - (self.height() - 200) / (y_axis_lines - 1)

    def draw_ticks(self, temporaldist, painter):
        """ Function to draw ticks at the axes """
        # scale axes to 1s (abscissae) and -20 dB (ordinate)
        painter.save()
        painter.scale(((self.width() - 200) / (len(self.timestep))), - ((
                                        self.height() - 200) / self.y_range))
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        # draw ticks for time-axis
        startpoint = 1
        for _ in range(0, len(self.timestep), 1):
            painter.drawLine(QtCore.QLineF(startpoint, 0., startpoint, - 1))
            startpoint += 1.
        # draw ticks for gain-axis
        y_axis = 0
        y_axis_lines = 5
        for _ in range(0, y_axis_lines):
            painter.drawLine(QtCore.QLineF(-0.08, y_axis, 0, y_axis))
            y_axis = y_axis + self.y_range / (y_axis_lines - 1)
        painter.restore()

    def draw_data(self, temporaldist, painter):
        """ Function to plot the data """
        painter.save()
        # scale abscissae to time interval between two sequent values
        painter.scale(((self.width() - 200) / (len(self.timeValue) /
                                           (self.temporaldist))
                                           * (1 / self.temporaldist)),
                                           -((self.height() - 200)
                                             / self.y_range))
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        brush = QtGui.QBrush(QtCore.Qt.blue)
        painter.setBrush(brush)
        # start at time 0 (on the right), draw to the left
        startpoint = 0
        for a in range(0, len(self.dBValue) - 1, 1):
            db = self.dBValue[a] + 80
            db2 = self.dBValue[a + 1] + 80
            painter.drawLine(QtCore.QLineF(startpoint, db, startpoint + 1,
                                            db2))
            startpoint = startpoint + 1
        painter.restore()

    # call function by PyQt
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        brush = QtGui.QBrush(QtCore.Qt.white)
        painter.setBrush(brush)
        painter.drawRect(100, 100, self.width() - 200, self.height() - 200)
        painter.setBrush(QtGui.QBrush())
        painter.setPen(pen)
        # draw abscissae (time-axis)
        painter.drawLine(100, 100, 100, self.height() - 100)
        # draw ordinate (gain-axis)
        painter.drawLine(100, self.height() - 100, self.width() - 100,
                         self.height() - 100)
        # set origin to the bottom left of the diagram
        painter.translate(100, self.height() - 100)
        self.draw_text(painter)
        self.draw_ticks(self.temporaldist, painter)
        self.draw_data(self.temporaldist, painter)
        painter.end()
        self.update()
