
from scipy import fftpack
from matplotlib import pyplot as plt
def task_func(arr):
    # Calculate the FFT for each row
    fft_results = [np.abs(fftpack.fft(row)) for row in arr]
    
    # Plot the results
    fig, ax = plt.subplots()
    for i, fft_result in enumerate(fft_results):
        ax.plot(fft_result, label=f'Row {i+1}')
    
    ax.set_xlabel('Index')
    ax.set_ylabel('Absolute FFT Coefficient')
    ax.set_title('FFT of Each Row')
    ax.legend()
    
    return ax