'''
Created on 01.06.2013

@author: Christopherus

Audiobuffer for audio analyser and using a ringbuffer.
'''


from ringbuffer import RingBuffer
from sound_device import SAMPLING_RATE as FS


FRAMES_PER_BUFFER = 1024


class AudioBuffer():
    def __init__(self, logger):
        self.ringbuffer = RingBuffer(logger)
        self.newpoints = 0
        self.delay_samples = 0

    def data(self, length):
        return self.ringbuffer.data(length)

    def data_older(self, length, delay_samples):
        return self.ringbuffer.data_older(length, delay_samples)

    def newdata(self):
        return self.data(self.newpoints)

    def set_newdata(self, newpoints):
        self.newpoints = newpoints

    def data_delayed(self, length):
        undelayed = self.data(length)
        delayed = self.data_older(length, self.delay_samples)
        data = delayed
        data[1, :] = undelayed[1, :]
        return data

    def set_delay_ms(self, delay_ms):
        self.delay_samples = delay_ms * 1e-3 * FS

    def data_indexed(self, start, length):
        return self.ringbuffer.data_indexed(start, length)
