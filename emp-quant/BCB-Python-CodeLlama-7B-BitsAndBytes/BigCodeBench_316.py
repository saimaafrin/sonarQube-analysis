
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    # Generate a list of random values within the specified range
    values = [random.randint(value_range[0], value_range[1]) for _ in range(100)]

    # Create a dictionary to store the counts for each category
    counts = {}
    for value in values:
        category = CATEGORIES[value % len(CATEGORIES)]
        if category not in counts:
            counts[category] = 0
        counts[category] += 1

    # Create a DataFrame from the counts dictionary
    df = pd.DataFrame(counts.items(), columns=['Category', 'Count'])

    return df