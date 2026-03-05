
import numpy as np
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(df, bins=4):
    # Calculate the histogram of the 'value' column
    counts, bins = np.histogram(df['value'], bins=bins)

    # Create a Counter object with the count of each duplicate value
    counter = Counter(df['value'])

    # Create a matplotlib.axes.Axes object to plot the histogram
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], counts, width=bins[1] - bins[0], color='#00FF0060')

    # Fit a normal distribution curve to the data and overlay it on the histogram
    x = np.linspace(bins[0], bins[-1], 100)
    y = norm.pdf(x, loc=np.mean(df['value']), scale=np.std(df['value']))
    ax.plot(x, y, color='#000000', linewidth=2)

    # Set the plot title, x-axis label, and y-axis label
    ax.set_title('Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Return the Counter object and the matplotlib.axes.Axes object
    return counter, ax