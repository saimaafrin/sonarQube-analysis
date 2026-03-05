import pandas as pd
import re
from scipy import stats
import matplotlib.pyplot as plt
def task_func(text):
    # Extract names not surrounded by square brackets
    names = re.findall(r'\b\w+\b', text)
    names = [name for name in names if not re.search(r'\[\w+\]', text)]
    
    # Count the frequency of each name
    name_freq = pd.Series(names).value_counts()
    
    # Create a bar chart of the name frequencies
    if not name_freq.empty:
        fig, ax = plt.subplots()
        name_freq.plot(kind='bar', ax=ax)
        plt.show()
    else:
        ax = None
    
    # Calculate skewness and kurtosis
    skewness = name_freq.skew() if not name_freq.empty else None
    kurtosis = name_freq.kurtosis() if not name_freq.empty else None
    
    return name_freq, ax, skewness, kurtosis