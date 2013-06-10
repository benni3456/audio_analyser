# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Terzpegelmesser_Version1_6.ui'
#
# Created: Mon Jun 10 20:19:54 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(924, 753)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.PlotTerzpegel = thirdPenStyles(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotTerzpegel.sizePolicy().hasHeightForWidth())
        self.PlotTerzpegel.setSizePolicy(sizePolicy)
        self.PlotTerzpegel.setMinimumSize(QtCore.QSize(200, 200))
        self.PlotTerzpegel.setObjectName(_fromUtf8("PlotTerzpegel"))
        self.horizontalLayout_2.addWidget(self.PlotTerzpegel)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.PlotKanalpegel = Channel_Bar(self.centralwidget)
        self.PlotKanalpegel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.PlotKanalpegel.setObjectName(_fromUtf8("PlotKanalpegel"))
        self.horizontalLayout_7.addWidget(self.PlotKanalpegel)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.PlotWellenform = PlotWaveform(self.centralwidget)
        self.PlotWellenform.setObjectName(_fromUtf8("PlotWellenform"))
        self.horizontalLayout_11.addWidget(self.PlotWellenform)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.PlotSpektrogramm = MatplotlibWidget(self.tab_3)
        self.PlotSpektrogramm.setObjectName(_fromUtf8("PlotSpektrogramm"))
        self.horizontalLayout.addWidget(self.PlotSpektrogramm)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.PlotFFT = MatplotlibWidget(self.tab_4)
        self.PlotFFT.setObjectName(_fromUtf8("PlotFFT"))
        self.horizontalLayout_6.addWidget(self.PlotFFT)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.labelFFT = QtGui.QLabel(self.tab_4)
        self.labelFFT.setObjectName(_fromUtf8("labelFFT"))
        self.verticalLayout_4.addWidget(self.labelFFT)
        self.BoxFFT = QtGui.QComboBox(self.tab_4)
        self.BoxFFT.setObjectName(_fromUtf8("BoxFFT"))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.BoxFFT.addItem(_fromUtf8(""))
        self.verticalLayout_4.addWidget(self.BoxFFT)
        self.labelMittel = QtGui.QLabel(self.tab_4)
        self.labelMittel.setObjectName(_fromUtf8("labelMittel"))
        self.verticalLayout_4.addWidget(self.labelMittel)
        self.BoxMittel = QtGui.QDoubleSpinBox(self.tab_4)
        self.BoxMittel.setObjectName(_fromUtf8("BoxMittel"))
        self.verticalLayout_4.addWidget(self.BoxMittel)
        self.labelBew = QtGui.QLabel(self.tab_4)
        self.labelBew.setObjectName(_fromUtf8("labelBew"))
        self.verticalLayout_4.addWidget(self.labelBew)
        self.BoxBew = QtGui.QComboBox(self.tab_4)
        self.BoxBew.setObjectName(_fromUtf8("BoxBew"))
        self.BoxBew.addItem(_fromUtf8(""))
        self.BoxBew.addItem(_fromUtf8(""))
        self.BoxBew.addItem(_fromUtf8(""))
        self.BoxBew.addItem(_fromUtf8(""))
        self.verticalLayout_4.addWidget(self.BoxBew)
        self.push_plus = QtGui.QPushButton(self.tab_4)
        self.push_plus.setMaximumSize(QtCore.QSize(25, 28))
        self.push_plus.setObjectName(_fromUtf8("push_plus"))
        self.verticalLayout_4.addWidget(self.push_plus)
        self.push_minus = QtGui.QPushButton(self.tab_4)
        self.push_minus.setMaximumSize(QtCore.QSize(25, 28))
        self.push_minus.setObjectName(_fromUtf8("push_minus"))
        self.verticalLayout_4.addWidget(self.push_minus)
        self.RadioLin = QtGui.QRadioButton(self.tab_4)
        self.RadioLin.setChecked(False)
        self.RadioLin.setObjectName(_fromUtf8("RadioLin"))
        self.verticalLayout_4.addWidget(self.RadioLin)
        self.RadioLog = QtGui.QRadioButton(self.tab_4)
        self.RadioLog.setChecked(True)
        self.RadioLog.setObjectName(_fromUtf8("RadioLog"))
        self.verticalLayout_4.addWidget(self.RadioLog)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.PlotGainVerlauf = GainPlotter(self.tab_5)
        self.PlotGainVerlauf.setObjectName(_fromUtf8("PlotGainVerlauf"))
        self.horizontalLayout_8.addWidget(self.PlotGainVerlauf)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.T = QtGui.QWidget()
        self.T.setObjectName(_fromUtf8("T"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.T)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.PlotTerzpegel_2 = thirdPenStyles(self.T)
        self.PlotTerzpegel_2.setObjectName(_fromUtf8("PlotTerzpegel_2"))
        self.horizontalLayout_10.addWidget(self.PlotTerzpegel_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.T, _fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.DeviceList = QtGui.QComboBox(self.centralwidget)
        self.DeviceList.setMaximumSize(QtCore.QSize(300, 30))
        self.DeviceList.setObjectName(_fromUtf8("DeviceList"))
        self.horizontalLayout_4.addWidget(self.DeviceList)
        self.ButtonStartStop = QtGui.QPushButton(self.centralwidget)
        self.ButtonStartStop.setMinimumSize(QtCore.QSize(100, 30))
        self.ButtonStartStop.setMaximumSize(QtCore.QSize(200, 30))
        self.ButtonStartStop.setObjectName(_fromUtf8("ButtonStartStop"))
        self.horizontalLayout_4.addWidget(self.ButtonStartStop)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDatei = QtGui.QMenu(self.menubar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Spektrogramm", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFFT.setText(QtGui.QApplication.translate("MainWindow", "FFT-Länge", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(0, QtGui.QApplication.translate("MainWindow", "32", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(1, QtGui.QApplication.translate("MainWindow", "64", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(2, QtGui.QApplication.translate("MainWindow", "128", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(3, QtGui.QApplication.translate("MainWindow", "256", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(4, QtGui.QApplication.translate("MainWindow", "512", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(5, QtGui.QApplication.translate("MainWindow", "1024", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(6, QtGui.QApplication.translate("MainWindow", "2048", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(7, QtGui.QApplication.translate("MainWindow", "4096", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(8, QtGui.QApplication.translate("MainWindow", "8192", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxFFT.setItemText(9, QtGui.QApplication.translate("MainWindow", "16384", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMittel.setText(QtGui.QApplication.translate("MainWindow", "Mittelungszeit [ms]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBew.setText(QtGui.QApplication.translate("MainWindow", "Bewertung", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxBew.setItemText(0, QtGui.QApplication.translate("MainWindow", "keine", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxBew.setItemText(1, QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxBew.setItemText(2, QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.BoxBew.setItemText(3, QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.push_plus.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.push_minus.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.RadioLin.setText(QtGui.QApplication.translate("MainWindow", "linear", None, QtGui.QApplication.UnicodeUTF8))
        self.RadioLog.setText(QtGui.QApplication.translate("MainWindow", "log", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "FFT", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Gain-Verlauf", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.T), QtGui.QApplication.translate("MainWindow", "Terzpegel", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonStartStop.setText(QtGui.QApplication.translate("MainWindow", "START/STOP", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatei.setTitle(QtGui.QApplication.translate("MainWindow", "Datei", None, QtGui.QApplication.UnicodeUTF8))

from plot_channellevel import Channel_Bar
from matplotlibwidget import MatplotlibWidget
from plot_gain import GainPlotter
from plot_waveform import PlotWaveform
from plot_terzpegel import thirdPenStyles
