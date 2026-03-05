
import csv
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def task_func(file_path):
    # Read the CSV file
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Calculate the sample mean and standard deviation
    sample = np.random.choice(data, size=30, replace=False)
    mean = np.mean(sample)
    std = np.std(sample, ddof=1)

    # Plot the histogram with a normal distribution curve
    fig, ax = plt.subplots()
    ax.hist(sample, bins='auto')
    x = np.linspace(min(sample), max(sample), 100)
    ax.plot(x, stats.norm.pdf(x, mean, std))
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram with Normal Distribution Curve')

    return mean, std, ax