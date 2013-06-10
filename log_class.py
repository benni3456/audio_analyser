'''
Created on 01.06.2013

@author: Christopherus
'''

from PyQt4 import QtCore

class Logger(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        
        self.count = 0
        self.log = ""

    # push some text to the log
    def push(self, text):
        if len(self.log)==0:
            self.log = "[0] %s" %text
        else:
            self.log = "%s\n[%d] %s" %(self.log, self.count, text)
        self.count += 1
        self.emit(QtCore.SIGNAL('logChanged'))

    # return the current log
    def text(self):
        return self.log