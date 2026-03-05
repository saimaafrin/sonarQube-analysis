
import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

def task_func(L, M, N, audio_file):
    # Check if audio file exists
    if not os.path.isfile(audio_file):
        raise FileNotFoundError(f"Audio file {audio_file} does not exist")

    # Read audio data from file
    data, sr = sf.read(audio_file)

    # Normalize data based on sound pressure level (SPL)
    spl = 20 * np.log10(np.sqrt(np.mean(data**2)))
    data = data / spl

    # Create MxN matrix from list L
    matrix = np.array(L).reshape(M, N)

    # Normalize matrix based on sound pressure level (SPL)
    matrix = matrix / spl

    # Generate spectrogram from matrix
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='inferno', aspect='auto', extent=(0, N, 0, M))
    ax.set_xlabel('Time')
    ax.set_ylabel('Frequency')
    ax.set_title('Spectrogram')
    ax.set_yscale('log')
    ax.set_xscale('linear')

    return matrix, fig