
import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np

def task_func(animals=None, seed=42):
    # Set the random seed for reproducibility
    random_seed(seed)

    # Create a dictionary to store the animal counts
    animal_counts = {}

    # Loop through each animal in the list
    for animal in animals:
        # Generate a random count for each animal
        count = randint(1, 100)

        # Add the count to the dictionary
        animal_counts[animal] = count

    # Calculate the mean, median, and standard deviation of the counts
    mean = statistics.mean(animal_counts.values())
    median = statistics.median(animal_counts.values())
    stddev = statistics.stdev(animal_counts.values())

    # Create a DataFrame with the animal counts
    df = pd.DataFrame(animal_counts, columns=['Animal', 'Count'])

    # Calculate the mean, median, and standard deviation of the counts
    df['Mean'] = mean
    df['Median'] = median
    df['Standard Deviation'] = stddev

    # Generate a bar chart of the counts
    fig, ax = plt.subplots()
    ax.bar(df['Animal'], df['Count'])
    ax.set_title('Animal Counts')
    ax.set_xlabel('Animal')
    ax.set_ylabel('Count')
    plt.show()

    return df