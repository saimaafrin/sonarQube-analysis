
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(df, bins=4):
    # Count duplicates in the 'value' column
    duplicates = df['value'].value_counts()
    duplicates = duplicates[duplicates > 1]
    duplicate_counter = Counter(duplicates)

    # Plot histogram with normal distribution curve
    fig, ax = plt.subplots()
    values = df['value'].values
    ax.hist(values, bins=bins, color='green', alpha=0.6, label='Data')
    mean, std = norm.fit(values)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    ax.plot(x, p, 'k', linewidth=2, label='Normal fit')
    ax.set_title('Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()

    return duplicate_counter, ax