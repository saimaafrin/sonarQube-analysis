
import pandas as pd
import re
from scipy import stats

def task_func(text):
    # Extract names from the text that are not surrounded by square brackets
    names = re.findall(r'[a-zA-Z]+', text)

    # Create a pandas Series with the frequency of each name
    name_freq = pd.Series(names).value_counts()

    # Create a bar chart of the name frequencies
    if len(names) > 0:
        fig, ax = plt.subplots()
        ax.bar(name_freq.index, name_freq.values, color='blue')
        ax.set_xlabel('Name')
        ax.set_ylabel('Frequency')
        ax.set_title('Name Frequencies')
        plt.show()
    else:
        fig = None

    # Calculate the skewness and kurtosis of the name frequencies
    skewness = stats.skewness(name_freq)
    kurtosis = stats.kurtosis(name_freq)

    return (name_freq, fig, skewness, kurtosis)