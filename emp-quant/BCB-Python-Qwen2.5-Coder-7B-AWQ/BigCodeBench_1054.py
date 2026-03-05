import csv
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
def task_func(file_path):
    try:
        # Read data from CSV file
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            population_data = [float(row[0]) for row in reader]
        
        # Sample 30 individuals from the population without replacement
        sample = np.random.choice(population_data, size=30, replace=False)
        
        # Calculate the mean and standard deviation of the sample
        sample_mean = np.mean(sample)
        sample_std = np.std(sample, ddof=1)
        
        # Generate a histogram of the sample data
        plt.figure(figsize=(10, 6))
        n, bins, patches = plt.hist(sample, bins='auto', density=True, alpha=0.6, color='g')
        
        # Overlay a normal distribution curve on the histogram
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = stats.norm.pdf(x, sample_mean, sample_std)
        plt.plot(x, p, 'k', linewidth=2)
        
        # Display the plot
        plt.show()
        
        # Return the sample mean, sample standard deviation, and the plot object
        return sample_mean, sample_std, plt
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")