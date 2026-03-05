
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(df, bins=4):
    # Count the occurrences of each value in the 'value' column
    value_counts = df['value'].value_counts()
    
    # Identify and count duplicate values
    duplicates = value_counts[value_counts > 1]
    duplicate_counter = Counter(duplicates)
    
    # Plot a histogram of the 'value' column
    fig, ax = plt.subplots()
    df['value'].plot(kind='hist', ax=ax, bins=bins, color='green', alpha=0.6)
    
    # Fit a normal distribution to the data
    x = df['value'].values
    mean, std = norm.fit(x)
    x = np.linspace(min(x), max(x), 100)
    p = norm.pdf(x, mean, std)
    ax.plot(x, p, "k", linewidth=2)
    
    # Set plot properties
    ax.set_title("Distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    
    # Return the Counter object and the Axes object
    return (duplicate_counter, ax)