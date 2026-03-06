
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(df, bins=4):
    # Count the number of duplicates in the 'value' column
    counter = Counter(df['value'])

    # Create a histogram of the 'value' column data
    fig, ax = plt.subplots()
    ax.hist(df['value'], bins=bins, alpha=0.6, color='green')

    # Fit a normal distribution curve to the data and overlay it on the histogram
    x = np.linspace(df['value'].min(), df['value'].max(), 100)
    y = norm.pdf(x, loc=df['value'].mean(), scale=df['value'].std())
    ax.plot(x, y, color='black', linewidth=2)

    # Set the plot title and labels
    ax.set_title('Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Return the counter and the axes object
    return counter, ax