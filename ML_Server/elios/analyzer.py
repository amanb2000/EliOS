import numpy as np
import pandas as pd

# Fourier Transformation Functions

# Constants:
sample_rate = 256 # Hz

def getLabeledFFT(col):
    len_seconds = len(col)/sample_rate
    fft = np.fft.fft(col)
    fft = np.abs(fft)**2 # Getting power spectrum of EEG
    fft = fft[:(len(fft)//2)]
    
    freqs = []
    
    for ind in range(0, len(fft)):
        freqs.append(ind*1/len_seconds)
    
    list_out = [freqs, fft]
    
    return list_out

def getBands(col, log=True):
    # alpha: 8-13hz
    # beta: 14-30hz
    # theta: 4-7hz
    # delta: 0.5-3hz
    # gamma: 31-50hz
    alpha = 0
    beta = 0
    theta = 0
    delta = 0
    gamma = 0
    
    num_alpha = 0
    num_beta = 0
    num_theta = 0
    num_delta = 0
    num_gamma = 0
    
    list_in = getLabeledFFT(col)
    freqs = list_in[0]
    amps = list_in[1]
    
    for i in range(len(freqs)):
        freq = freqs[i]
        if(freq > 0.5 and freq < 4):
            delta += amps[i]
            num_delta += 1
        elif(freq < 8):
            theta += amps[i]
            num_theta += 1
        elif(freq < 14):
            alpha += amps[i]
            num_alpha += 1
        elif(freq < 31):
            beta += amps[i]
            num_beta += 1
        elif(freq < 51):
            gamma += amps[i]
            num_gamma += 1
    
    ret_dict = {
        "alpha": (alpha/num_alpha),
        "beta": (beta/num_beta),
        "theta": (theta/num_theta),
        "delta": (delta/num_delta),
        "gamma": (gamma/num_gamma),
        "R": ((alpha/num_alpha)/(beta/num_beta))
    }
    
    '''
        In addition, according to previous research [23], definite interrelations exist between α and β activities. 
        For example, α activity indicates that the brain is in a state of relaxation, whereas β activity is related 
        to stimulation. In the study mentioned previously, to observe continuous changes in the mental state of the 
        subjects, the ratio of α and β activities was used as the feature for assessing the level of mental 
        attentiveness. This study produced the following feature value using the same principle:
    '''
    
    if(log):
        for key, value in ret_dict.items():
            ret_dict[key] = np.log(value)
    
    return ret_dict

def aggregate_all_bands(inp):
    dicts = [getBands(inp['eeg1']), getBands(inp['eeg2']), getBands(inp['eeg3']), getBands(inp['eeg4']), getBands(inp['eeg5(aux)'])]
    ret_dict = {"alpha": 0, "beta": 0, "theta": 0, "delta": 0, "gamma": 0, "R": 0}
    
    for i in dicts:
        ret_dict['alpha'] += (1/5) * i['alpha']
        ret_dict['beta'] += (1/5) * i['beta']
        ret_dict['gamma'] += (1/5) * i['gamma']
        ret_dict['delta'] += (1/5) * i['delta']
        ret_dict['theta'] += (1/5) * i['theta']
        ret_dict['R'] += (1/5) * i['R']
    
    return ret_dict