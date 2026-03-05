import pandas as pd
import re
from scipy import stats
def task_func(text):
    """
    Extracts all names from a given text string that are not surrounded by square brackets and counts the frequency of each extracted name. It then creates a bar chart of the name frequencies and returns the name frequencies as a pandas Series and the bar chart plot's axes object along with the skewness and kurtosis of the name frequencies. If the skewness and kurtosis are nan, they are returned as None.
    """
    # Extract names from text
    names = re.findall(r'[^\[]+', text)

    # Create a pandas Series with the frequency of each name
    name_freq = pd.Series(names).value_counts()

    # Create a bar chart of the name frequencies
    if len(name_freq) > 0:
        name_freq.plot(kind='bar')
        axes = name_freq.plot(kind='bar').axes
    else:
        axes = None

    # Calculate the skewness and kurtosis of the name frequencies
    skewness = stats.skew(name_freq)
    kurtosis = stats.kurtosis(name_freq)

    # Return the name frequencies as a pandas Series, the bar chart plot's axes object, the skewness, and the kurtosis
    return name_freq, axes, skewness, kurtosis
text = "This is a test string with names [John] and [Jane] in it."