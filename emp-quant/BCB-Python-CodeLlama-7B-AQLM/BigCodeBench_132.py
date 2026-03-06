import binascii
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def task_func(hex_str):
    """
    Converts a hex string representation into actual bytes and records the frequency of each byte value.
    The function supports hex strings with or without '\\x' prefix.

    Parameters:
    - hex_str (str): The hex string (e.g., 'F3BE8080' or '\\xF3\\xBE\\x80\\x80').

    Returns:
    - tuple: A tuple containing a pandas DataFrame of byte frequencies with columns ['Byte Value', 'Frequency']
             and a matplotlib Axes object for the plot with 'Byte Value' as the X-axis and 'Frequency' as the Y-axis.

    Raises:
    - ValueError: If 'hex_str' is not a valid hex string.

    Requirements:
    - binascii
    - numpy
    - matplotlib.pyplot
    - pandas

    Example:
    >>> df, ax = task_func('F3BE8080')
    >>> print(df)
       Byte Value  Frequency
    0         128          2
    1         190          1
    2         243          1
    >>> plt.show()
    """
    # Check if 'hex_str' is a valid hex string
    if not is_valid_hex_str(hex_str):
        raise ValueError('Invalid hex string')

    # Convert hex string to bytes
    bytes_str = binascii.unhexlify(hex_str)

    # Convert bytes to numpy array
    bytes_arr = np.frombuffer(bytes_str, dtype=np.uint8)

    # Count the frequency of each byte value
    byte_freq = bytes_arr.astype(np.uint8).reshape(-1).tolist()
    byte_freq = pd.DataFrame(byte_freq, columns=['Byte Value'])
    byte_freq['Frequency'] = byte_freq['Byte Value'].value_counts()

    # Plot the byte frequencies
    ax = byte_freq.plot.bar(x='Byte Value', y='Frequency', rot=0)

    return byte_freq, ax