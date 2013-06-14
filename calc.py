# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:56:40 2013

@author: be2257
"""
import numpy as np


def rms(arr):
    """ calculates the rms power of an array """
    return np.sqrt(np.mean(np.power(arr, 2)))


def dB(power):
    """ calculates the logarithmic dB value of a power """
    return 20 * np.log10(power)