
import csv
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def task_func(file_path):
    # Read the CSV file
    with open(file_path, 'r') as f:
        data = [float(line) for line in f]

    # Sample 30 values without replacement
    sample = np.random.choice(data, 30, replace=False)

    # Calculate mean and standard deviation
    mean = np.mean(sample)
    std = stats.sem(sample, axis=0)

    # Plot a histogram with a normal distribution curve
    fig, ax = plt.subplots()
    ax.hist(sample, bins=30, normed=True, alpha=0.5, label='Sample')
    ax.plot(stats.norm.pdf(stats.norm.cdf(stats.norm.ppf(0, mean, std), mean, std)), label='Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Sample')
    ax.legend()
    plt.show()

    return mean, std, ax