# -*- coding: utf-8 -*-
"""
This code creates a plot in a window-function
The plot displays the count of thirds
Created on Mon Apr 29 15:00:40 2013

@author: fabim
"""

#!/usr/bin/python

# penstyles.py
from __future__ import division
import sys
from PyQt4 import QtGui, QtCore
#from pylab import


class thirdPenStyles(QtGui.QWidget):
    '''plot thirds in window
    '''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 200, 1000, 500)
        self.setWindowTitle('graphic')
        self.y_anzahl = 80
        self.y_ticks = range(-80, 20, 20)
        self.sidespace = 50
        self.setMinimumSize(200, 200)
        self.freqValue = [29]
        self.dBValue = [29]

    def readArray(self, dBValue, freqValue):
        '''reads data to draw from input device
        '''
        assert (len(dBValue) == len(freqValue))
        self.dBValue = dBValue
        self.freqValue = freqValue

    def draw_text(self, painter):
        '''draws the text of the axis
        '''
        painter.drawText(QtCore.QRectF(self.width() - self.sidespace * 2, 0,
                                       20, 20), QtCore.Qt.AlignCenter, 'fm')
        painter.drawText(QtCore.QRectF(-30, -self.height() + self.sidespace +
                                    20, 20, 20), QtCore.Qt.AlignCenter, 'dB')
        lesstext = 1
        textspace = (self.width() - self.sidespace * 2) / (len(self.freqValue))
        startpoint = 0.5 * textspace
        while textspace < 25:
            textspace = textspace * 2
            lesstext = lesstext * 2
        for i in range(0, len(self.freqValue), lesstext):
            painter.drawText(QtCore.QRectF(startpoint - textspace / 2, 0,
                                         textspace, 20), QtCore.Qt.AlignCenter,
                                         str(int(self.freqValue[i])))
                                            #x-Achse Beschriftung
            startpoint = startpoint + textspace
        count_ticks = 5
        y_axis = -10
        for i in range(0, count_ticks):
            painter.drawText(QtCore.QRectF(-30, y_axis, 20, 20),
                             QtCore.Qt.AlignCenter, str(self.y_ticks[i]))
            #y achse beschriftung
            y_axis = y_axis - ((self.height() - self.sidespace * 2) /
                                                    (count_ticks - 1))

    def draw_ticks(self, rectspace, painter):
        '''
        draws the ticks of the axis
        '''
        painter.save()
        painter.scale(((self.width() - self.sidespace * 2) /
                                (len(self.freqValue))), 1)
        # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        startpoint = 0
        #Schleife für x-Achse
        for a in range(0, len(self.dBValue), 1):
            painter.drawLine(QtCore.QLineF(startpoint + (rectspace / 2), 0,
                                           startpoint + (rectspace / 2), 3))
            #x achse einheiten striche
            startpoint = startpoint + rectspace
        painter.restore()
        painter.save()
        painter.scale(1, -((self.height() - self.sidespace * 2) /
                           self.y_anzahl))
        # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        y_axis = 0
        anzahl_striche = 5
        for b in range(0, anzahl_striche):
            painter.drawLine(QtCore.QLineF(-5, y_axis, 0, y_axis))
            #y achse einheiten striche
            y_axis = y_axis + self.y_anzahl / (anzahl_striche - 1)
        painter.restore()

    def draw_data(self, rectspace, painter):
        '''
        draws data into the plot axis
        '''
        painter.save()
        painter.scale(((self.width() - self.sidespace * 2) /
                       (len(self.freqValue))), - ((self.height() -
                                self.sidespace * 2) / self.y_anzahl))
        # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        brush = QtGui.QBrush(QtCore.Qt.green)
        painter.setBrush(brush)
        startpoint = 0
        for a in range(0, len(self.dBValue), 1):
            db = self.dBValue[a]
            if db < -80:
                db = -80
            painter.drawRect(QtCore.QRectF(startpoint, 0, rectspace, 80 + db))
            #balken
            startpoint = startpoint + rectspace
        painter.restore()

    def paintEvent(self, event):
        '''main function
        '''
        painter = QtGui.QPainter()
        painter.begin(self)
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        brush = QtGui.QBrush(QtCore.Qt.white)
        painter.setBrush(brush)
        painter.drawRect(self.sidespace, self.sidespace, self.width() -
                                    self.sidespace * 2, self.height() -
                                    self.sidespace * 2)
        painter.setBrush(QtGui.QBrush())
        painter.setPen(pen)
        painter.drawLine(self.sidespace, self.sidespace, self.sidespace,
                                            self.height() - self.sidespace)
        # x-Axis frequency
        painter.drawLine(self.sidespace, self.height() - self.sidespace,
                         self.width() - self.sidespace, self.height() -
                        self.sidespace)
        #y-Axis dB
        painter.translate(self.sidespace, self.height() - self.sidespace)
        # Koordinatensystem auf 0 Punkt der Grafik
        self.draw_text(painter)
        rectspace = 1
        self.draw_ticks(rectspace, painter)
        self.draw_data(rectspace, painter)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dt = thirdPenStyles()
    dt.readArray(dBValue, freqValue)
    dt.show()
    app.exec_()
