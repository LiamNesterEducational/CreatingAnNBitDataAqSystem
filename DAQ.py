#### Main DAQ file

from os import system
system('clear')

import numpy as np
import math
import matplotlib.pyplot as plt
import random

import Resolution as R
import VoltageFraction as VF
import FrequencyGeneration as FG
import FilteredSignal as FS

#############################################################################

## These are based on the measurment system
UpperVoltage = 10 # V
LowerVoltage = -10 # V

## These are set by the user
BitNumber = 2
ActiveVoltage = 10 # V

MainActiveFrequencyHz = 0.5 # Hz
MainActiveFrequency = MainActiveFrequencyHz*2*math.pi

#############################################################################

## Empty Matrices

size = 1111

MATRIX = np.zeros((size,5), dtype = float)

#############################################################################

Res = R.ResolutionFunc(UpperVoltage, LowerVoltage, BitNumber)
VoltFrac = VF.VoltageFractionFunc(ActiveVoltage, UpperVoltage, LowerVoltage)

## Loop for solving
for x in range(size):
    t = x/100 # generates time step
    MAIN = FG.MainVoltageSignal(ActiveVoltage, MainActiveFrequency, t) # generates main signal
    NOISE = random.uniform(-1,1)/10 # generates some noise
    TotalSignal = MAIN+NOISE # saves total signal
    FilteredSignal = FS.FilteredSignalFunc(TotalSignal, VoltFrac, BitNumber, Res, LowerVoltage, UpperVoltage)
    Error = abs(TotalSignal-FilteredSignal)

    MATRIX[x,0] = t
    MATRIX[x,1] = TotalSignal
    MATRIX[x,2] = FilteredSignal
    MATRIX[x,3] = Error
    MATRIX[x,4] = NOISE

#############################################################################

x = MATRIX[:,0]
y1 = MATRIX[:,1]
y2 = MATRIX[:,2]

plt.plot(x, y1, label='Unfiltered')
plt.plot(x, y2, label='Filtered')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

y3 = MATRIX[:,3]

plt.plot(x, y3, label='Error')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

print("Complete...")