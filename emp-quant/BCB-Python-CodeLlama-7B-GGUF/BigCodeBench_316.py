
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    # Generate a random number within the specified range
    random_number = random.randint(value_range[0], value_range[1])

    # Determine the category based on the random number
    category = CATEGORIES[random_number // 25]

    # Create a DataFrame with the category and count
    df = pd.DataFrame({'Category': [category], 'Count': [1]})

    return df