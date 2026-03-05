
import binascii
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(hex_str):
    # Check if the input is a valid hex string
    if not binascii.hexify(hex_str).isalnum():
        raise ValueError("Invalid hex string")

    # Convert the hex string to bytes
    bytes_list = binascii.unhexlify(hex_str)

    # Calculate the frequency of each byte value
    byte_freq = np.bincount(bytes_list)

    # Create a pandas DataFrame with the byte frequencies
    df = pd.DataFrame({'Byte Value': byte_freq.tolist(), 'Frequency': byte_freq.tolist()})

    # Plot the byte frequencies
    fig, ax = plt.subplots()
    ax.bar(df['Byte Value'], df['Frequency'])
    ax.set_xlabel('Byte Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Byte Frequencies')

    return df, fig