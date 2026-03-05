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

    # Create a list of animals
    if animals is None:
        animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra']

    # Create a dictionary to store the counts for each animal
    animal_counts = {}
    for animal in animals:
        animal_counts[animal] = []

    # Generate 10 random counts for each animal
    for _ in range(10):
        for animal in animals:
            animal_counts[animal].append(randint(1, 100))

    # Calculate the mean, median, and standard deviation of the counts
    means = {}
    medians = {}
    stds = {}
    for animal in animals:
        means[animal] = statistics.mean(animal_counts[animal])
        medians[animal] = statistics.median(animal_counts[animal])
        stds[animal] = statistics.stdev(animal_counts[animal])

    # Create a DataFrame with the statistics
    df = pd.DataFrame({'Animal': animals, 'Mean': means, 'Median': medians, 'Standard Deviation': stds})

    # Generate a bar chart of the counts
    fig, ax = plt.subplots()
    ax.bar(animals, animal_counts[animals])
    ax.set_title('Counts of Animals in the Zoo')
    ax.set_xlabel('Animal')
    ax.set_ylabel('Count')
    ax.set_xticks(np.arange(len(animals)))
    ax.set_xticklabels(animals)
    plt.show()

    return df