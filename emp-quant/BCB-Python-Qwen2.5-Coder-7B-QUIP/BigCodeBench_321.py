
import pandas as pd
import re
from scipy import stats

def task_func(text):
    # Extract names that are not surrounded by square brackets
    names = re.findall(r'\b[A-Za-z]+\b', text)
    
    # Count the frequency of each name
    name_freq = pd.Series(names).value_counts()
    
    # Create a bar chart of the name frequencies
    if not name_freq.empty:
        axes = name_freq.plot(kind='bar')
    else:
        axes = None
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(name_freq, nan_policy='nan')
    kurtosis = stats.kurtosis(name_freq, nan_policy='nan')
    
    return name_freq, axes, skewness, kurtosis