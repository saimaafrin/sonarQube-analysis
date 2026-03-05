
import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

def task_func(L, M, N, audio_file):
    # Load audio file
    try:
        data, sr = sf.read(audio_file)
    except FileNotFoundError:
        raise FileNotFoundError("Specified audio file does not exist")

    # Normalize data
    data = data / np.max(data)

    # Calculate SPL
    spl = 20 * np.log10(np.sqrt(np.mean(data ** 2)))

    # Generate spectrogram
    t, f = librosa.core.spectrogram(data, sr)

    # Plot spectrogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(t, f, cmap='inferno', norm=LogNorm(vmin=0, vmax=spl))
    ax.set_xlabel('Time')
    ax.set_ylabel('Frequency')
    ax.set_title('Spectrogram')
    fig.show()

    return data, fig