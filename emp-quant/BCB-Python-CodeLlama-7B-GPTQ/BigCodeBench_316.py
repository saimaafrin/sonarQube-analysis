import pandas as pd
import random
CATEGORIES = ['A', 'B', 'C', 'D', 'E']
def task_func(value_range=(0, 100)):
    """
    Generate a category distribution within a specified range and return as a DataFrame.
    """
    # Initialize a dictionary to store the counts of each category
    counts = {}

    # Generate random values within the specified range
    for _ in range(1000):
        value = random.randint(value_range[0], value_range[1])

        # Determine the category based on the value
        category = CATEGORIES[value // 20]

        # Increment the count of the category
        counts[category] = counts.get(category, 0) + 1

    # Create a DataFrame with the counts
    df = pd.DataFrame({'Category': CATEGORIES, 'Count': [counts[category] for category in CATEGORIES]})

    return df