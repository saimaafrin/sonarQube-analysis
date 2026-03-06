
import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

def task_func(L, M, N, audio_file):
    # Check if the audio file exists
    if not os.path.isfile(audio_file):
        raise FileNotFoundError("Audio file does not exist")

    # Read the audio data from the file
    data, sr = sf.read(audio_file)

    # Normalize the data based on the sound pressure level (SPL)
    spl = 20 * np.log10(np.sqrt(np.mean(data**2)))
    data = data / spl

    # Create an MxN matrix from the normalized data
    matrix = np.reshape(data, (M, N))

    # Generate a spectrogram from the matrix
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='inferno', extent=(0, N, 0, M))
    ax.set_xlabel('Time')
    ax.set_ylabel('Frequency')
    ax.set_title('Spectrogram')
    ax.set_xscale('log')
    ax.set_yscale('linear')
    ax.set_ylim([0, M])
    ax.set_xlim([0, N])
    ax.set_aspect('auto')
    fig.tight_layout()

    return matrix, fig

# Display the spectrogram
plt.show()