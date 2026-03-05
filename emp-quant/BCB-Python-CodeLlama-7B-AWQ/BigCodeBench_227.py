import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt
def task_func(L, M, N, audio_file):
    """
    Creates an MxN matrix from a list L, normalizes it based on the sound pressure level (SPL) of a specified audio file, and generates a spectrogram from the matrix.
    SPL = 20 * log10(sqrt(mean(data^2))) where 'data' is the audio data read from the file.
    The spectrogram is displayed with a logarithmic scale for frequency and a linear scale for time, with the SPL used to adjust the amplitude displayed in the spectrogram.
    """
    # Check if the audio file exists
    if not os.path.isfile(audio_file):
        raise FileNotFoundError(f"{audio_file} does not exist")

    # Read the audio data from the file
    data, sr = sf.read(audio_file)

    # Normalize the data based on the sound pressure level (SPL)
    SPL = 20 * np.log10(np.sqrt(np.mean(data**2)))
    data = data / SPL

    # Create an MxN matrix from the normalized data
    matrix = np.reshape(data, (M, N))

    # Generate a spectrogram from the matrix
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap="inferno", aspect="auto", extent=[0, M, 0, N])
    ax.set_xlabel("Time")
    ax.set_ylabel("Frequency")
    ax.set_title("Spectrogram")
    ax.set_xlim([0, M])
    ax.set_ylim([0, N])
    ax.set_xticks(np.arange(0, M, 10))
    ax.set_yticks(np.arange(0, N, 10))
    ax.set_xticklabels(np.arange(0, M, 10))
    ax.set_yticklabels(np.arange(0, N, 10))
    ax.set_xscale("log")
    ax.set_yscale("linear")
    fig.tight_layout()

    return matrix, fig
L = [1, 2, 3, 4, 5]
M = 5
N = 10
audio_file = "audio.wav"