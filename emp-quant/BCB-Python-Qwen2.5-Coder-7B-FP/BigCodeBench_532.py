import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(df, bins=4):
    # Count duplicates in the 'value' column
    duplicates = df['value'].value_counts()
    duplicates = duplicates[duplicates > 1]
    
    # Plot histogram and normal distribution curve
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(df['value'], bins=bins, color='green', alpha=0.6)
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, np.mean(df['value']), np.std(df['value']))
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set plot title and labels
    ax.set_title('Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    return (Counter(duplicates), ax)