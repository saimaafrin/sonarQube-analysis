
import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def task_func(L):
    # Initialize an empty list to store the random integers
    random_ints = []

    # Iterate over the nested lists in L
    for nested_list in L:
        # Get the number of rows and columns from the nested list
        num_rows, num_cols = nested_list

        # Generate a random integer between 1 and 100 for each cell in the DataFrame
        random_ints.append(np.random.randint(RANGE[0], RANGE[1], size=(num_rows, num_cols)))

    # Create a DataFrame from the list of random integers
    df = pd.DataFrame(random_ints)

    return df