import pandas as pd
import re
from scipy import stats
def task_func(text):
    # Regular expression to find names not surrounded by square brackets
    pattern = r'(?<!\[)\b\w+\b(?!\])'
    names = re.findall(pattern, text)
    
    # Count the frequency of each name
    name_counts = pd.Series(pd.value_counts(names))
    
    # Create a bar chart of the name frequencies
    if not name_counts.empty:
        ax = name_counts.plot(kind='bar')
    else:
        ax = None
    
    # Calculate skewness and kurtosis
    skewness = name_counts.skew() if not name_counts.empty else None
    kurtosis = name_counts.kurtosis() if not name_counts.empty else None
    
    return name_counts, ax, skewness, kurtosis