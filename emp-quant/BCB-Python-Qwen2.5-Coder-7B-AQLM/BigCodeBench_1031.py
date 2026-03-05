
import random
import string
import pandas as pd
import matplotlib.pyplot as plt

def task_func(n_rows=1000):
    if n_rows <= 0:
        raise ValueError("n_rows must be greater than 0")
    
    # Generate random 3-letter strings
    strings = [''.join(random.choices(string.ascii_lowercase, k=3)) for _ in range(n_rows)]
    
    # Create a DataFrame to count the frequency of each string
    df = pd.DataFrame(strings, columns=['string'])
    frequency = df['string'].value_counts().head(30)
    
    # Plot the histogram
    ax = frequency.plot(kind='bar', figsize=(12, 8))
    ax.set_title('Frequency of Top 30 Unique 3-Letter Strings')
    ax.set_xlabel('3-Letter String')
    ax.set_ylabel('Frequency')
    
    return ax