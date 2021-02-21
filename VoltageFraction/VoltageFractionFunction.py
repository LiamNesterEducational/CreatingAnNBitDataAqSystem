## Resolution Function

def VoltageFractionFunc(ActiveSignal, UpperV, LowerV):
    VF = (ActiveSignal - LowerV)/(UpperV - LowerV) # some function
    return(VF)