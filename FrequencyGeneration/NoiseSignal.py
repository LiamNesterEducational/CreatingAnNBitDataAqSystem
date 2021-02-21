## Noise Voltage Singal Function

import math

def NoiseVoltageSignal(NoiseAmp, ActiveFreq, time):
    NVS = NoiseAmp*math.sin(ActiveFreq*time)
    return(NVS)