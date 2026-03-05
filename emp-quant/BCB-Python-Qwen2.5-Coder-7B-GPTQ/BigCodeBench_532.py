import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(df, bins=4):
    # Count duplicates in the 'value' column
    duplicates = df['value'].value_counts()
    duplicate_counts = Counter(duplicates[duplicates > 1])

    # Plotting the histogram
    fig, ax = plt.subplots()
    ax.hist(df['value'], bins=bins, color='green', alpha=0.6)
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(df['value'])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Setting plot title and labels
    ax.set_title('Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    return duplicate_counts, ax