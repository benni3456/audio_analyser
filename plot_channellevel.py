# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:00:40 2013

@author: ol2172
"""

#!/usr/bin/python

# penstyles.py
from __future__ import division
import sys
from PyQt4 import QtGui, QtCore
from pylab import randn


class Channel_Bar(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 200, 1000, 500)
        self.setMinimumSize(50, 50)
        self.setWindowTitle('graphic')
        self.y_anzahl = 80
        self.y_ticks = range(-80, 20, 20)
        self.side_space = 50
        self.freq_value = [0]
        self.db_value = [0] * 0
    # read input data arrays

    def readArray(self, db_value, freq_value):

        assert (len(db_value) == len(freq_value))
        self.db_value = db_value
        self.freq_value = freq_value

    def draw_text(self, painter):
        painter.drawText(QtCore.QRectF(self.width() - self.side_space * 2, 0,
                                40, 20), QtCore.Qt.AlignCenter, 'channel')
        painter.drawText(QtCore.QRectF(-30, -self.height() + self.side_space
                                       + 20, 50, 20), QtCore.Qt.AlignCenter,
                                        'level [dB]')
        lesstext = 1
        textspace = (self.width() - self.side_space *
                     2) / (len(self.freq_value))
        startpoint = 0.5 * textspace
        while textspace < 25:
            textspace = textspace * 2
            lesstext = lesstext * 2

        for i in range(0, len(self.freq_value), lesstext):
            painter.drawText(QtCore.QRectF(startpoint -
                        textspace / 2, 0, textspace, 20),
                        QtCore.Qt.AlignCenter, str(int(self.freq_value[i])))
                        # x-Achse Beschriftung
            startpoint = startpoint + textspace

        count_ticks = 5
        y_axis = -10
        for i in range(0, count_ticks):
            painter.drawText(QtCore.QRectF(-30, y_axis, 20, 20),
                    QtCore.Qt.AlignCenter | QtCore.Qt.TextDontClip,
                    str(self.y_ticks[i]))
                    #y achse beschriftung
            y_axis = y_axis - (self.height() - self.side_space * 2) / (
                                                        count_ticks - 1)

    def draw_ticks(self, balkenbreite, painter):

        painter.save()
        painter.scale(((self.width() - self.side_space *
                        2) / (len(self.freq_value))), 1)
                        # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))

        startpoint = 0
        #Schleife für x-Achse
        for _ in range(0, len(self.db_value), 1):
            painter.drawLine(QtCore.QLineF(startpoint + (balkenbreite / 2), 0,
                                           startpoint + (balkenbreite / 2), 3))
                                            #x achse einheiten striche
            startpoint = startpoint + balkenbreite
        painter.restore()
        painter.save()
        #print("self.y_anzahl %s" %self.y_anzahl)
        painter.scale(1, - ((self.height() - self.side_space *
                             2) / self.y_anzahl))
                            # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))

        y_axis = 0
        anzahl_striche = 5
        for _ in range(0, anzahl_striche):
            painter.drawLine(QtCore.QLineF(-5, y_axis, 0, y_axis))
                #y achse einheiten striche
            y_axis = y_axis + self.y_anzahl / (anzahl_striche - 1)
        painter.restore()

    def draw_data(self, balkenbreite, painter):
        painter.save()
        painter.scale(((self.width() - self.side_space *
                        2) / (len(self.freq_value))), - ((self.height() -
                                        self.side_space * 2) / self.y_anzahl))
                        # Skalieren auf Anzahl der Werte
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 0))
        startpoint = 0
        for a in range(0, len(self.db_value), 1):
            db = self.db_value[a]

            if db < -80:
                db = -80

            if db > -10:
                brush = QtGui.QBrush(QtCore.Qt.red)

            else:
                brush = QtGui.QBrush(QtCore.Qt.green)

            painter.setBrush(brush)

            painter.drawRect(QtCore.QRectF(startpoint, 0, balkenbreite,
                                           80 + db))
                                            #balken
            startpoint = startpoint + balkenbreite
        painter.restore()

    def paintEvent(self, event):
        painter = QtGui.QPainter()

        painter.begin(self)

        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        brush = QtGui.QBrush(QtCore.Qt.white)
        painter.setBrush(brush)
        painter.drawRect(self.side_space, self.side_space, self.width()
                    - self.side_space * 2, self.height() - self.side_space * 2)
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
        balkenbreite = 1
        self.draw_ticks(balkenbreite, painter)
        self.draw_data(balkenbreite, painter)

        painter.end()
        self.update()


if __name__ == '__main__':

    db_value = -(abs(randn(2)) * 10 + 0)
    #db_value = range(1, 30)*random.randint(10, 60)
    freqValue = range(1, 3)
    print (freqValue)
    print (db_value)

    app = QtGui.QApplication(sys.argv)
    dt = Channel_Bar()

    dt.readArray(db_value, freqValue)

    dt.show()
    app.exec_()
