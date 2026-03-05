
import pandas as pd
import re
from scipy import stats

def task_func(text):
    # Extract names that are not surrounded by square brackets
    names = re.findall(r'(?<!\[)\b\w+\b(?!\])', text)

    # Create a pandas Series with the frequency of each name
    name_freq = pd.Series(names).value_counts()

    # Create a bar chart of the name frequencies
    if len(name_freq) > 0:
        name_freq.plot(kind='bar')
        plt.title('Name Frequencies')
        plt.xlabel('Name')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print('No names found')

    # Calculate the skewness and kurtosis of the name frequencies
    skewness = stats.skew(name_freq)
    kurtosis = stats.kurtosis(name_freq)

    # Return the name frequencies as a pandas Series and the bar chart plot's axes object
    return name_freq, plt.gca(), skewness, kurtosis