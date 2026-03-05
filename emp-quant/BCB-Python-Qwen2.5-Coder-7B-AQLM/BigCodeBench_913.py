
from typing import List, Union
import numpy as np
import scipy.fft

def task_func(data: List[Union[int, str]], repetitions: int = 1) -> dict:
    if not data or repetitions <= 0:
        return {'mode': np.array([]), 'count': np.array([])}
    
    # Repeat the data
    repeated_data = data * repetitions
    
    # Calculate the mode(s)
    unique, counts = np.unique(repeated_data, return_counts=True)
    mode = unique[np.argmax(counts)]
    mode_counts = counts[np.argmax(counts)]
    
    # Calculate the Fast Fourier Transform (FFT)
    fft_result = scipy.fft.fft(repeated_data)
    
    return {'mode': np.array([mode]), 'count': np.array([mode_counts]), 'fft': fft_result}