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
        raise FileNotFoundError(f"Audio file {audio_file} does not exist.")

    # Read the audio data from the file
    data, sr = sf.read(audio_file)

    # Calculate the sound pressure level (SPL)
    spl = 20 * np.log10(np.sqrt(np.mean(data ** 2)))

    # Create an MxN matrix from the list L
    matrix = np.array(L).reshape(M, N)

    # Normalize the matrix based on the SPL
    normalized_matrix = matrix / spl

    # Generate a spectrogram from the normalized matrix
    spectrogram = librosa.feature.spectrogram(normalized_matrix, sr=sr, n_mels=256, n_perseg=128)

    # Display the spectrogram with a logarithmic scale for frequency and a linear scale for time
    fig, ax = plt.subplots()
    ax.imshow(spectrogram, cmap="inferno", extent=[0, 1, 0, 1])
    ax.set_xlabel("Time")
    ax.set_ylabel("Frequency")
    ax.set_title("Spectrogram")
    plt.show()

    return normalized_matrix, fig
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M = 3
N = 3
audio_file = "audio.wav"