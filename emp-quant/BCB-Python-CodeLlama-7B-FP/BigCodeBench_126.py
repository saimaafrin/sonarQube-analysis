import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
def task_func(animals=None, seed=42):
    """
    Generate a report on the number of animals in a zoo.
    For each animal, generate a random count within a specified range,
    calculate the mean, median, and standard deviation of these counts,
    and return a DataFrame with these statistics.
    Additionally, generate a bar chart of the counts.
    Note that:
    - The mode is not included in the returned DataFrame due to the possibility of no repeating values in the randomly generated counts.
    - The function should output with:
        DataFrame: A pandas DataFrame with columns ['Animal', 'Mean', 'Median', 'Standard Deviation'].
        Each animal's count is randomly generated 10 times within the range 1 to 100, inclusive.
    """
    # Set the random seed for reproducibility
    random_seed(seed)

    # Create a dictionary to store the counts for each animal
    animal_counts = {}

    # Generate 10 random counts for each animal
    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        animal_counts[animal] = counts

    # Calculate the mean, median, and standard deviation of the counts
    means = [statistics.mean(counts) for counts in animal_counts.values()]
    medians = [statistics.median(counts) for counts in animal_counts.values()]
    stds = [statistics.stdev(counts) for counts in animal_counts.values()]

    # Create a DataFrame with the statistics
    df = pd.DataFrame({
        'Animal': list(animal_counts.keys()),
        'Mean': means,
        'Median': medians,
        'Standard Deviation': stds
    })

    # Generate a bar chart of the counts
    fig, ax = plt.subplots()
    ax.bar(df['Animal'], df['Count'])
    ax.set_xlabel('Animal')
    ax.set_ylabel('Count')
    ax.set_title('Counts of Animals in the Zoo')
    plt.show()

    return df
animals = ['Lion', 'Tiger', 'Bear', 'Monkey', 'Giraffe']