
import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np

def task_func(animals=None, seed=42):
    # Set the random seed for reproducibility
    random_seed(seed)

    # Create a list of animals
    animals = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'monkey', 'snake', 'frog', 'crocodile', 'leopard']

    # Initialize the DataFrame with the animal names
    df = pd.DataFrame(animals, columns=['Animal'])

    # Generate the counts for each animal
    for animal in animals:
        counts = []
        for i in range(10):
            counts.append(randint(1, 100))
        df[animal] = counts

    # Calculate the mean, median, and standard deviation of the counts
    df['Mean'] = df.mean(axis=1)
    df['Median'] = df.median(axis=1)
    df['Standard Deviation'] = df.std(axis=1)

    # Generate a bar chart of the counts
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df.index, df['Count'])
    ax.set_xlabel('Animal')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Animal Counts')
    plt.show()

    return df