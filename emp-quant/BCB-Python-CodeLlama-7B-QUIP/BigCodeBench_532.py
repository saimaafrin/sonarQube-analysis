
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(df, bins=4):
    # Identify and count duplicate values in the 'value' column
    counts = Counter(df['value'])

    # Plot a histogram for all values in the 'value' column
    fig, ax = plt.subplots()
    ax.hist(df['value'], bins=bins, color='green', alpha=0.6)

    # Overlay a normal distribution curve on the histogram
    x = np.linspace(min(df['value']), max(df['value']), 100)
    y = norm.pdf(x, mean=np.mean(df['value']), var=np.var(df['value']))
    ax.plot(x, y, 'k', linewidth=2)

    # Set the plot title and labels
    ax.set_title("Distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    return counts, fig