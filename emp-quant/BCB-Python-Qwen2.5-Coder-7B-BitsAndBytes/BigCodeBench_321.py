
import pandas as pd
import re
from scipy import stats

def task_func(text):
    # Extract names using regex that are not surrounded by square brackets
    names = re.findall(r'\b\w+\b', text)
    
    # Filter out names that are surrounded by square brackets
    filtered_names = [name for name in names if '[' not in name and ']' not in name]
    
    # Count the frequency of each name
    name_counts = pd.Series(filtered_names).value_counts()
    
    # Create a bar chart of the name frequencies
    if not name_counts.empty:
        ax = name_counts.plot(kind='bar')
    else:
        ax = None
    
    # Calculate skewness and kurtosis
    skewness = name_counts.skew() if not name_counts.empty else None
    kurtosis = name_counts.kurtosis() if not name_counts.empty else None
    
    return name_counts, ax, skewness, kurtosis