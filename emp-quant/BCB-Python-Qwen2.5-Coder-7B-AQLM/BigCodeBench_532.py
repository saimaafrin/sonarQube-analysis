
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(df, bins=4):
    # Count duplicates in the 'value' column
    duplicates = df['value'].duplicated(keep=False)
    duplicate_values = df.loc[duplicates, 'value']
    value_counts = Counter(duplicate_values)
    
    # Plot histogram and normal distribution curve
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(df['value'], bins=bins, color='green', alpha=0.6)
    mu, std = norm.fit(df['value'])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    ax.set_title('Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    return value_counts, ax