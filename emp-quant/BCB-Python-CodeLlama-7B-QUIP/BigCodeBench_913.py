
from typing import List, Union
import numpy as np
import scipy.fft

def task_func(data: List[Union[int, str]], repetitions: int = 1):
    if not data or repetitions <= 0:
        return {}

    # Calculate the mode(s) and count(s)
    mode_counts = np.bincount(data)
    mode_indices = np.argpartition(mode_counts, -repetitions)
    modes = data[mode_indices]
    counts = mode_counts[mode_indices]

    # Calculate the fast Fourier transform
    fft_data = np.array(data)
    fft_data = fft_data.repeat(repetitions)
    fft_data = np.abs(scipy.fft.fft(fft_data))

    return {
        'mode': modes,
        'count': counts,
        'fft': fft_data
    }