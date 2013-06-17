# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:31:26 2013

@author: be2257
"""


from numpy import diff, sign, where


class Oszi:
    def __init__(self, PlotOszi, audiobuffer, NumberOfPeriods):
        self.PlotOszi = PlotOszi
        self.audiobuffer = audiobuffer
        # number of periods to be displayed
        self.NumberOfPeriods = NumberOfPeriods
        # undersampling factor; default=1
        self.resample = 1

    def findperiod(self, dat, NumberOfPeriods):
        ''' function that computes and returns possible period length
            within given data
        '''

        # extracts audio data from list; possible downsampling by factor
        # self.resample
        data = dat[0][::self.resample]
        # finds all zero crossings in data vector
        zero_crossings = where(diff(sign(data)))
        self.NumberOfPeriods = NumberOfPeriods

        # always returns the ascending slope of the period starting with
        # the third period
        if data[zero_crossings[0][0]] > data[zero_crossings[0][1]]:
            # in case of odd slope
            if len(zero_crossings[0]) < (1 + self.NumberOfPeriods * 2):
                return [zero_crossings[0][1], zero_crossings[0][-1]]
            else:
                return [zero_crossings[0][1], zero_crossings[0][1 +
                                                self.NumberOfPeriods * 2]]
        else:
            # in case of even slope
            if len(zero_crossings[0]) < (self.NumberOfPeriods * 2):
                return [zero_crossings[0][1], zero_crossings[0][-1]]
            else:
                return [zero_crossings[0][0], zero_crossings[0][
                                            self.NumberOfPeriods * 2]]

    def plot(self, NumberOfPeriods):
        ''' function to plot the waveform '''
        data = self.audiobuffer.newdata()
        self.NumberOfPeriods = NumberOfPeriods
        # calls function for indices of starting- and endpoint of
        # self.NumberOfPeriods periods of the input vector
        zero_crossings = self.findperiod(data, self.NumberOfPeriods)

        # plots self.NumberOfPeriods periods of the input vector


        self.PlotOszi.readArray(data[0][zero_crossings[0]:self.resample *
                                        zero_crossings[1]:self.NumberOfPeriods])
