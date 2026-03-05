import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
def task_func(animals=None, seed=42):
    """
    Create a report on the number of animals in a zoo. For each animal, generate a random count within a specified range, calculate the mean, median, and standard deviation of these counts, and return a DataFrame with these statistics. Additionally, generate a bar chart of the counts.
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

    # Generate random counts for each animal
    for animal in animals:
        counts = []
        for _ in range(10):
            counts.append(randint(1, 100))
        animal_counts[animal] = counts

    # Calculate the mean, median, and standard deviation of the counts for each animal
    means = []
    medians = []
    stds = []
    for animal, counts in animal_counts.items():
        means.append(statistics.mean(counts))
        medians.append(statistics.median(counts))
        stds.append(statistics.stdev(counts))

    # Create a DataFrame with the results
    df = pd.DataFrame({
        'Animal': animals,
        'Mean': means,
        'Median': medians,
        'Standard Deviation': stds
    })

    # Generate a bar chart of the counts
    fig, ax = plt.subplots()
    ax.bar(animals, animal_counts.values())
    ax.set_ylabel('Count')
    ax.set_title('Animal Counts')
    plt.show()

    return df
animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra']