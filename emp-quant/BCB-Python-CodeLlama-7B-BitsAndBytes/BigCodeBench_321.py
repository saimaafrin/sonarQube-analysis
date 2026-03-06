
import pandas as pd
import re
from scipy import stats

def task_func(text):
    # Extract names from text that are not surrounded by square brackets
    names = re.findall(r'[^\[]+(?=\])', text)

    # Create a pandas Series with the frequency of each name
    name_freq = pd.Series(names).value_counts()

    # Create a bar chart of the name frequencies
    if len(name_freq) > 0:
        fig, ax = plt.subplots()
        ax.bar(name_freq.index, name_freq.values)
        ax.set_title('Name Frequencies')
        ax.set_xlabel('Name')
        ax.set_ylabel('Frequency')
        plt.show()
    else:
        fig = None
        ax = None

    # Calculate the skewness and kurtosis of the name frequencies
    skewness = stats.skew(name_freq) if len(name_freq) > 0 else None
    kurtosis = stats.kurtosis(name_freq) if len(name_freq) > 0 else None

    return (name_freq, fig, ax, skewness, kurtosis)