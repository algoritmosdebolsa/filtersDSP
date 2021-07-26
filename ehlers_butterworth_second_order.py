from __dsp__ import Filter
import numpy as np

def main() -> None:
    
### Ehlers 2nd order Butterworth filter ###
    fs = 1
    pc = 10 # Critical period
    a1 = np.exp(-np.sqrt(2)*np.pi/(fs*pc))
    b1 = 2*a1*np.cos(np.sqrt(2)*np.pi/(fs*pc))
    c2 = b1
    c3 = -a1*a1
    c1 = 1 - c2 - c3
        
    filt = Filter(name = "Ehlers 2nd order Butterworth filter", 
                  NumeratorZcoefs = [c1], 
                  DenominatorZcoefs = [1,-c2,-c3], 
                  comments = "")
    
    # filt.plotNormFreqResponse()
    # filt.plotFreqResponse()
    filt.plotPeriodResponse()
    # filt.plotPhaseResponse()
    filt.plotGroupDelay()

if __name__ == '__main__':
    main()