
import csv
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def task_func(file_path):
    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [float(row[0]) for row in reader]

    # Randomly select 30 individuals from the population
    sample = np.random.choice(data, size=30, replace=False)

    # Calculate the mean and standard deviation of the sample
    mean = np.mean(sample)
    std = np.std(sample, ddof=1)

    # Plot the histogram of the sample data
    fig, ax = plt.subplots()
    ax.hist(sample, bins='auto')

    # Overlay a normal distribution curve on the histogram
    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = stats.norm.pdf(x, mean, std)
    ax.plot(x, y)

    # Set the title and labels of the plot
    ax.set_title('Histogram of Sample Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Return the sample mean, standard deviation, and the matplotlib subplot
    return mean, std, ax

# Print the results
print(f'Sample mean: {mean:.2f}')
print(f'Sample standard deviation: {std:.2f}')

# Plot the histogram and normal distribution curve
ax.figure.show()