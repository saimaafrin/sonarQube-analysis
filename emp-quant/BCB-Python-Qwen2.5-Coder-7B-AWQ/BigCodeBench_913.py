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
    mode = unique[counts == counts.max()]

    # Calculate the count(s) of the mode(s)
    count = counts[counts == counts.max()]

    # Calculate the fast fourier transform
    fft_result = scipy.fft.fft(repeated_data)

    return {'mode': mode, 'count': count}
data = [1, 2, 2, 3, 3, 3]
repetitions = 3