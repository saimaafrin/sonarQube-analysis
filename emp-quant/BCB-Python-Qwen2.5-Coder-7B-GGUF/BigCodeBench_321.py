
import pandas as pd
import re
from scipy import stats
import matplotlib.pyplot as plt

def task_func(text):
    # Extract names not surrounded by square brackets
    names = re.findall(r'\b[A-Za-z]+\b', text)
    
    # Count the frequency of each name
    name_counts = pd.Series(names).value_counts()
    
    # Create a bar chart of the name frequencies
    if not name_counts.empty:
        fig, ax = plt.subplots()
        name_counts.plot(kind='bar', ax=ax)
        plt.title('Name Frequencies')
        plt.xlabel('Names')
        plt.ylabel('Frequency')
    else:
        fig, ax = None, None
    
    # Calculate skewness and kurtosis
    skewness = name_counts.skew() if not name_counts.empty else None
    kurtosis = name_counts.kurtosis() if not name_counts.empty else None
    
    return name_counts, ax, skewness, kurtosis