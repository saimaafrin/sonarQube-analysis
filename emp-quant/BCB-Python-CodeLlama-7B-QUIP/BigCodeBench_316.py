
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    # Generate a random number within the specified range
    random_number = random.randint(value_range[0], value_range[1])

    # Determine which category the number belongs to
    category = None
    for i in range(len(CATEGORIES)):
        if random_number <= value_range[1] * i / len(CATEGORIES):
            category = CATEGORIES[i]
            break

    # Create the DataFrame
    data = {'Category': [category], 'Count': [1]}
    df = pd.DataFrame(data)

    return df