import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt
def task_func(L, M, N, audio_file):
    # Check if the audio file exists
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"The specified audio file '{audio_file}' does not exist.")
    
    # Read the audio data from the file
    audio_data, sample_rate = sf.read(audio_file)
    
    # Calculate the sound pressure level (SPL)
    spl = 20 * np.log10(np.sqrt(np.mean(audio_data**2)))
    
    # Create an MxN matrix from the list L
    matrix = np.array(L).reshape(M, N)
    
    # Normalize the matrix based on the SPL
    normalized_matrix = matrix / (10**(spl/20))
    
    # Generate a spectrogram from the normalized matrix
    fig, ax = plt.subplots()
    librosa.display.specshow(normalized_matrix, sr=sample_rate, x_axis='time', y_axis='log', ax=ax)
    
    # Adjust the amplitude displayed in the spectrogram based on the SPL
    ax.set_title(f'Spectrogram with SPL: {spl:.2f} dB')
    
    return normalized_matrix, fig