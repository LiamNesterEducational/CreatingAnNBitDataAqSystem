## Main Voltage Singal Function

def FilteredSignalFunc(InputSignal, VoltageFrac, BitNum, Resolution, LowerV, UpperV):
    FIRST = InputSignal- LowerV
    SECOND = FIRST / (UpperV - LowerV)
    THIRD = round(SECOND*(2**BitNum),0)
    FOURTH = THIRD*Resolution
    FiltSig = FOURTH + LowerV
    return(FiltSig)