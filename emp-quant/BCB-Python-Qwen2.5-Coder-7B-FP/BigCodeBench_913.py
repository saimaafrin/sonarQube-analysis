from typing import List, Union
import numpy as np
import scipy.fft
def task_func(data: List[Union[int, str]], repetitions: int = 1) -> dict:
    if not data or repetitions <= 0:
        return {'mode': np.array([]), 'count': np.array([])}

    # Repeat the data
    repeated_data = data * repetitions

    # Calculate the mode(s)
    mode, count = np.unique(repeated_data, return_counts=True)

    # Sort the mode(s) in ascending order
    sorted_indices = np.argsort(mode)
    mode = mode[sorted_indices]
    count = count[sorted_indices]

    # Calculate the Fast Fourier Transform (FFT)
    fft_result = scipy.fft.fft(repeated_data)

    return {'mode': mode, 'count': count, 'fft': fft_result}