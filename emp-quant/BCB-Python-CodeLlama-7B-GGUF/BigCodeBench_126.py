
import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np

def task_func(animals=None, seed=42):
    # Set the random seed for reproducibility
    random_seed(seed)

    # Create a dictionary to store the animal counts
    animal_counts = {}

    # Iterate over the animals
    for animal in animals:
        # Generate 10 random counts for each animal
        counts = [randint(1, 100) for _ in range(10)]

        # Calculate the mean, median, and standard deviation of the counts
        mean = statistics.mean(counts)
        median = statistics.median(counts)
        stddev = statistics.stdev(counts)

        # Add the animal and its statistics to the dictionary
        animal_counts[animal] = [mean, median, stddev]

    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(animal_counts, orient='index')

    # Rename the columns
    df.columns = ['Mean', 'Median', 'Standard Deviation']

    # Return the DataFrame
    return df