import random
import string
import pandas as pd
import matplotlib.pyplot as plt
def task_func(n_rows=1000):
    if n_rows <= 0:
        raise ValueError("n_rows must be greater than 0")
    
    # Generate random 3-letter strings
    strings = [''.join(random.choices(string.ascii_lowercase, k=3)) for _ in range(n_rows)]
    
    # Count the frequency of each string
    string_counts = pd.Series(strings).value_counts()
    
    # Get the top 30 most common strings
    top_30_strings = string_counts.head(30)
    
    # Plot the histogram
    ax = top_30_strings.plot(kind='bar', figsize=(12, 8))
    ax.set_xlabel('3-letter Strings')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Top 30 Unique 3-letter Strings')
    
    return ax