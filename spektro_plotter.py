from pylab import *
from calc import *
from scipy.signal import butter, lfilter
from sound_device import SAMPLING_RATE as fs
from plot_terzpegel import thirdPenStyles

class SpektroPlotter:
    def __init__(self, PlotSpektro, audiobuffer, fs=48000):
        ''' function that computes and plots (third) octave levels 
        of given input data 
        '''
        self.PlotSpektro = PlotSpektro
        self.audiobuffer = audiobuffer
        self.fs = fs
        self.weight = 0
        
        # computes frequencies and puts them in arrays
        self.fc = [1000.0 * (2.0 ** (1.0 / 3.0 * kk)) for kk in range(-15,13)]
        self.fu = [freq * (2.0 ** (-1.0 / 6.0)) for freq in self.fc]
        self.fo = [freq * (2.0 ** (1.0 / 6.0)) for freq in self.fc]

        # computes b,a-coefficients for each frequency band
        self.b = []
        self.a = []
        for freq in range(len(self.fc)):
            b,a = self.butterbandpass(self.fo[freq],self.fu[freq],self.fs,2)
            self.b.append(b)
            self.a.append(a)

        self.frequenzbewertung_a = [-39.4,-34.6,-30.2,-26.2,-22.5,-19.1,-16.1,
                                    -13.4,-10.9,-8.6,-6.6,-4.8,-3.2,-1.9,-0.8,
                                    0.0,0.6,1.0,1.2,1.3,1.2,1.0,0.5,-0.1,-1.1,
                                    -2.5,-4.3,-6.6]
                                    
        self.frequenzbewertung_c = [-3.0,-2.0,-1.3,-0.8,-0.5,-0.3,-0.2,-0.1,
                                    0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.1,
                                    -0.2,-0.3,-0.5,-0.8,-1.3,-2.0,-3.0,-4.4,
                                    -6.2,-8.5]
                                    

    def butterbandpass(self,fo,fu,fs,order=2):
        ''' function that computes a,b coefficients 
        of SOS butterworth bandpass 
        '''
        nyq = 0.5 * self.fs
        low = fu / nyq
        high = fo / nyq
        b, a = butter(order, [low, high], btype='bandpass', analog=False)
        return b,a

    def plot(self,weight):
        data = self.audiobuffer.newdata()
        ''' function to obtain and plot the third octave level '''
        self.weight = weight
        self.block = array(data,dtype=float64)
        self.thirdpow = []

        if self.weight == 1:
            self.frequenzbewertung =  self.frequenzbewertung_a
        elif self.weight == 2:
            self.frequenzbewertung =  self.frequenzbewertung_c
        else:
            self.frequenzbewertung = [0.0]*len(self.fc)

        # obtainment of the third octave levels
        for freq in range(len(self.fc)):
            freqpow = (dB(rms(lfilter(self.b[freq], self.a[freq], 
                                     self.block[:])[0])) + 
                                     self.frequenzbewertung[freq])
            self.thirdpow.append(freqpow)

        self.PlotSpektro.readArray(self.thirdpow,self.fc)

        