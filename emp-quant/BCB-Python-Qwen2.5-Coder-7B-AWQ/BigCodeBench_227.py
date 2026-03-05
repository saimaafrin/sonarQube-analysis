import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt
def task_func(L, M, N, audio_file):
    # Check if the audio file exists
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"The specified audio file '{audio_file}' does not exist.")
    
    # Read the audio data
    audio_data, sample_rate = sf.read(audio_file)
    
    # Calculate the sound pressure level (SPL)
    spl = 20 * np.log10(np.sqrt(np.mean(audio_data**2)))
    
    # Normalize the matrix based on the SPL
    normalized_matrix = np.array(L).astype(np.float32) / spl
    
    # Reshape the matrix to MxN
    normalized_matrix = normalized_matrix.reshape(M, N)
    
    # Generate the spectrogram
    fig, ax = plt.subplots()
    librosa.display.specshow(normalized_matrix, x_axis='time', y_axis='log', sr=sample_rate, ax=ax)
    ax.set_title(f'Spectrogram with SPL: {spl:.2f} dB')
    
    return normalized_matrix, fig