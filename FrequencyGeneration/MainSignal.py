## Main Voltage Singal Function

import math

def MainVoltageSignal(ActiveV, ActiveFreq, time):
    MVS = ActiveV*math.sin(ActiveFreq*time)
    return(MVS)