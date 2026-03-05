
import csv
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def task_func(file_path):
    try:
        # Read the population data from the CSV file
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            population_data = np.array(list(reader), dtype=float)

        # Sample 30 values from the population without replacement
        sample = np.random.choice(population_data, size=30, replace=False)

        # Calculate the mean and standard deviation of the sample
        sample_mean = np.mean(sample)
        sample_std = np.std(sample, ddof=1)

        # Plot the histogram of the sample
        fig, ax = plt.subplots()
        ax.hist(sample, bins='auto', density=True, alpha=0.6, color='g')

        # Overlay a normal distribution curve
        x = np.linspace(sample_mean - 3 * sample_std, sample_mean + 3 * sample_std, 100)
        ax.plot(x, stats.norm.pdf(x, sample_mean, sample_std), 'r-', lw=2)

        # Return the sample mean, sample standard deviation, and the plot
        return sample_mean, sample_std, ax

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None