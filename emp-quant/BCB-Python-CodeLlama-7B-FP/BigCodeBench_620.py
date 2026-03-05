import numpy as np
import pandas as pd
RANGE = (1, 100)
def task_func(L):
    """
    Generates a DataFrame filled with random integers.
    The dimensions of the DataFrame (number of rows and columns) are determined by multiplying pairs of integers from nested lists within the input list of lists 'L'.
    """
    # Initialize an empty list to store the random integers
    random_ints = []

    # Iterate over the nested lists in 'L'
    for nested_list in L:
        # Initialize an empty list to store the random integers for the current nested list
        nested_random_ints = []

        # Iterate over the integers in the current nested list
        for i in nested_list:
            # Generate a random integer within the specified range
            random_int = np.random.randint(RANGE[0], RANGE[1])

            # Add the random integer to the list of random integers for the current nested list
            nested_random_ints.append(random_int)

        # Add the list of random integers for the current nested list to the list of all random integers
        random_ints.append(nested_random_ints)

    # Convert the list of lists of random integers to a DataFrame
    df = pd.DataFrame(random_ints)

    # Return the DataFrame
    return df
L = [[1, 2], [3, 4], [5, 6]]