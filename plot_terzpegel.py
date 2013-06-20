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
        self.setMinimumSize(100, 100)
        self.setWindowTitle('graphic')
        self.y_anzahl = 80
        self.y_ticks = range(-80, 20, 20)
        self.side_space = 50
        self.freq_value = [29]
        self.db_value = [29]

    def readArray(self, db_value, freq_value):
        '''reads data to draw from input device
        '''
        assert (len(db_value) == len(freq_value))
        self.db_value = db_value
        self.freq_value = freq_value

    def frequency_formatter(self, f):
        if f < 1000:
            return(str(int(f)))
        else:
            return("%2.1fk"%(f/1000))

    def draw_text(self, painter):
        '''draws the text of the axis
        '''
        painter.drawText(QtCore.QRectF(self.width() - self.side_space * 2, 0,
                                       20, 20), QtCore.Qt.AlignCenter,
                         u"ƒm")
        painter.drawText(QtCore.QRectF(-30, -self.height() + self.side_space +
                                    20, 20, 20), QtCore.Qt.AlignCenter, 'dB')
        less_text = 1
        text_space = (self.width() - self.side_space * 2) / (len(self.freq_value))
        start_point = 0.5 * text_space
        while text_space < 30:
            text_space = text_space * 2
            less_text = less_text * 2

        for i in range(0, len(self.freq_value), less_text):
            painter.drawText(QtCore.QRectF(start_point - text_space / 2, 0,
                                         text_space, 20), QtCore.Qt.AlignCenter,
                                         self.frequency_formatter(self.freq_value[i]))
                                            #x-Achse Beschriftung
            start_point = start_point + text_space
        count_ticks = 5
        y_axis = -10
        for i in range(0, count_ticks):
            painter.drawText(QtCore.QRectF(-30, y_axis, 20, 20),
                             QtCore.Qt.AlignCenter, str(self.y_ticks[i]))
            #y achse beschriftung
            y_axis = y_axis - ((self.height() - self.side_space * 2) /
                                                    (count_ticks - 1))
#    print unichr(131)
    def draw_ticks(self, rectspace, painter):
        '''
        draws the ticks of the axis
        '''
        painter.save()
        painter.scale(((self.width() - self.side_space * 2) /
                                (len(self.freq_value))), 1)
        # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        start_point = 0
        #Schleife für x-Achse
        for a in range(0, len(self.db_value), 1):
            painter.drawLine(QtCore.QLineF(start_point + (rectspace / 2), 0,
                                           start_point + (rectspace / 2), 3))
            #x achse einheiten striche
            start_point = start_point + rectspace
        painter.restore()
        painter.save()
        painter.scale(1, -((self.height() - self.side_space * 2) /
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
        painter.scale(((self.width() - self.side_space * 2) /
                       (len(self.freq_value))), - ((self.height() -
                                self.side_space * 2) / self.y_anzahl))
        # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        brush = QtGui.QBrush(QtCore.Qt.green)
        painter.setBrush(brush)
        startpoint = 0
        for a in range(0, len(self.db_value), 1):
            db = self.db_value[a]
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
        painter.drawRect(self.side_space, self.side_space, self.width() -
                                    self.side_space * 2, self.height() -
                                    self.side_space * 2)
        painter.setBrush(QtGui.QBrush())
        painter.setPen(pen)
        painter.drawLine(self.side_space, self.side_space, self.side_space,
                                            self.height() - self.side_space)
        # x-Axis frequency
        painter.drawLine(self.side_space, self.height() - self.side_space,
                         self.width() - self.side_space, self.height() -
                        self.side_space)
        #y-Axis dB
        painter.translate(self.side_space, self.height() - self.side_space)
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
