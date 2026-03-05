
import random
import string
import pandas as pd
import matplotlib.pyplot as plt

def task_func(n_rows=1000):
    if n_rows <= 0:
        raise ValueError("n_rows must be greater than 0")
    
    # Generate random 3-letter strings
    letters = string.ascii_lowercase
    strings = [''.join(random.choices(letters, k=3)) for _ in range(n_rows)]
    
    # Count the frequency of each string
    freq = pd.Series(strings).value_counts()
    
    # Get the top 30 most common strings
    top_30 = freq.head(30)
    
    # Plot the histogram
    ax = top_30.plot(kind='bar', figsize=(10, 6))
    ax.set_xlabel('3-letter strings')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 30 Most Frequent 3-letter Strings')
    
    return ax