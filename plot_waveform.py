# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:00:40 2013

@author: ol2172
"""

from __future__ import division
import sys
from PyQt4 import QtGui, QtCore
from pylab import *



class PlotWaveform(QtGui.QWidget):
    """
    Draw a plot for waveform (Oszilloskop) for the current time

    The plot is drawn centered on the widget with smaller width/height as the
    widget itself. If the widget is not square, the smaller dimension is used.
    """


    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 200, 1000, 500)
        self.setWindowTitle('graphic')
        self.y_range = 2
        self.y_ticks = [-1, 0, 1]
        self.side_space = 50
        self.y_step = 3
        self.amplitude = (-rand(31) + rand(31))
        #self.amplitude = range(1, 30)*random.randint(10, 60)
        self.timeValue = range(-30, 1)


    def readArray(self, amplitude):
        # read input data arrays
        #assert (len(amplitude) == len(timeValue))
        self.amplitude = amplitude
        #self.timeValue = timeValue
        #print amplitude

    def draw_text(self, painter):
        painter.drawText(QtCore.QRectF(-30,
                        -(self.height()-2 * self.side_space) / 2-20, 40, 20),
                         QtCore.Qt.AlignCenter, 'signal')
        painter.drawText(QtCore.QRectF(self.width() - self.side_space * 2,
                        (self.height()-2 * self.side_space) / 2, 20, 20),
                         QtCore.Qt.AlignCenter, 'time')
        start_point = 0
        x_step_size = ((self.width() - self.side_space * 2) /
                     (len(self.timeValue)))
        for i in range(0, len(self.timeValue), 1):
            # label x-axis
            painter.drawText(QtCore.QRectF(start_point - x_step_size / 2,
                            (self.height() - 2 * self.side_space) / 2,
                            x_step_size, 20),
                             QtCore.Qt.AlignCenter, str(self.timeValue[i]))
            start_point = (start_point + (self.width() - self.side_space * 2) /
                          (len(self.timeValue)))
        y_axis = (self.height()-2 * self.side_space) / 2
        painter.drawText(QtCore.QRectF(-30, y_axis - 25, 20, 20),
                         QtCore.Qt.AlignCenter, 'min')
        y_axis = (y_axis - (self.height() - self.side_space * 2) /
                 (self.y_step - 1))
        # label y-axis
        painter.drawText(QtCore.QRectF(-30, y_axis - 10, 20, 20),
                         QtCore.Qt.AlignCenter, str(self.y_ticks[1]))
        y_axis = (y_axis - (self.height() - self.side_space * 2) /
                 (self.y_step - 1))
        painter.drawText(QtCore.QRectF(-30, y_axis + 5, 20, 20),
                         QtCore.Qt.AlignCenter, 'max')

    def draw_ticks(self, painter):
        painter.save()
        # scale number of value
        painter.scale(((self.width() - self.side_space * 2) /
                       (len(self.timeValue))), 1)
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        for a in range(0, len(self.amplitude) - 1):
            # draw ticks of x-axis
            painter.drawLine(QtCore.QLineF(a + 1, (self.height() - 2 *
                                                   self.side_space) / 2,
                                           a + 1, (self.height() - 2 *
                                                   self.side_space) / 2 + 3))
        painter.restore()   
        painter.save()
        # scale number of value
        painter.scale(1, -(self.height() - 2 * self.side_space - 30) / 2)
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        # draw ticks of y-axis
        for b in (-1, 0, 1):
            painter.drawLine(QtCore.QLineF(-5, b, 0, b))
        painter.restore()

    def draw_data(self, painter):
        painter.save()
        painter.scale(((self.width() - self.side_space * 2) /
                       (len(self.timeValue))),
                      - ((self.height() - self.side_space * 2 - 30) /
                         self.y_range))
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        brush = QtGui.QBrush(QtCore.Qt.blue)
        painter.setBrush(brush)
        start_point = 31
        end_point = 30
        for a in range(0, len(self.amplitude), 1):
            db = self.amplitude[a]
            db_last = self.amplitude[(a - 1)]
            painter.drawLine(QtCore.QLineF(start_point, db_last,
                                           end_point, db))
            start_point = start_point - 1
            end_point = end_point - 1
        painter.restore()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        brush = QtGui.QBrush(QtCore.Qt.white)
        painter.setBrush(brush)
        painter.drawRect(self.side_space, self.side_space,
                         self.width() - self.side_space * 2,
                         self.height() - self.side_space * 2)
        painter.setBrush(QtGui.QBrush())
        painter.setPen(pen)
        # x-axis time
        painter.drawLine(self.side_space, self.side_space, self.side_space,
                         self.height() - self.side_space)
        # y-axis signal
        painter.drawLine(self.side_space, self.height() - self.side_space,
                         self.width() - self.side_space,
                         self.height() - self.side_space)
        # point zero of the coordinate system on graph
        painter.translate(self.side_space, self.height() / 2)
        self.draw_text(painter)
        self.draw_ticks(painter)
        self.draw_data(painter)
        painter.end()
        self.update()

#===============================================================================
# if __name__== '__main__':
#        
#     amplitude = (-rand(31) + rand(31))
#     amplitude = range(1, 30)*random.randint(10, 60)
#     timeValue = range(-30, 1)
#     print (timeValue)
#     print len(amplitude)
# 
#     app = QtGui.QApplication(sys.argv)
#     dt = plot_waveform()
#     
#      dt.readArray(amplitude, timeValue)
#      
#      dt.show()
#      app.exec_()
#===============================================================================
 
